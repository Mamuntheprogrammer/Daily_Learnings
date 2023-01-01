import pyHook

def on_keyboard_event(event):
    # Print the key that was pressed
    print(event.Key)
    # Return True to pass the event to other handlers
    return True

# Create a hook manager
hook_manager = pyHook.HookManager()
# Register the on_keyboard_event callback for all keyboard events
hook_manager.KeyDown = on_keyboard_event
# Hook the keyboard
hook_manager.HookKeyboard()
# Start the event loop
pythoncom.PumpMessages()
