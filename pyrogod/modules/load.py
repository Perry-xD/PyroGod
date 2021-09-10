
# (C) 2021 Paramendra Singh

import os
from importlib import import_module, reload
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers.handler import Handler
from pyrogod import LOGGER, app
from pyrogod.modules.help import add_command_help
from config import PREFIX

add_command_help(
        "load", [
        ["`load`", "loads the replied plugin"],
               ],
)
@app.on_message(filters.command("load", PREFIX) & filters.me)
async def load_plugin(client: Client, message: Message):
    status_message = await message.edit("...")
    try:
        if message.reply_to_message is not None:
            down_loaded_plugin_name = await message.reply_to_message.download(
                file_name="./pyrogod/modules/"
            )
            if down_loaded_plugin_name is not None:
                # LOGGER.info(down_loaded_plugin_name)
                relative_path_for_dlpn = os.path.relpath(
                    down_loaded_plugin_name,
                    os.getcwd()
                )
                # LOGGER.info(relative_path_for_dlpn)
                lded_count = 0
                path = Path(relative_path_for_dlpn)
                module_path = ".".join(
                    path.parent.parts + (path.stem,)
                )
                # LOGGER.info(module_path)
                module = reload(import_module(module_path))
                # https://git.io/JvlNL
                for name in vars(module).keys():
                    # noinspection PyBroadException
                    try:
                        handler, group = getattr(module, name).handler

                        if isinstance(handler, Handler) and isinstance(group, int):
                            client.add_handler(handler, group)
                            LOGGER.info(
                                '[{}] [LOAD] {}("{}") in group {} from "{}"'.format(
                                    client.session_name,
                                    type(handler).__name__,
                                    name,
                                    group,
                                    module_path
                                )
                            )
                            lded_count += 1
                    except Exception:
                        pass
                await status_message.edit(
                    f"Loaded {lded_count} in PyroGod"
                )
    except Exception as error:
        await status_message.edit(
            f"ERROR: <code>{error}</code>"
        )
