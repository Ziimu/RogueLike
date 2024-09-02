(https://rogueliketutorials.com/tutorials/tcod/v2/part-7/)   ---POOLIK!!!

Edit main.py like this: (siit alla ~50%)

Diff Original
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
+           root_console.clear()
+           engine.event_handler.on_render(console=root_console)
+           context.present(root_console)
-           engine.render(console=root_console, context=context)

+           engine.event_handler.handle_events(context)
-           engine.event_handler.handle_events()