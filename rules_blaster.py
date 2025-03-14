import os
import sys
import time

from pynput import keyboard
from decoratorOperations import throttle

class RulesBlasterService:
    LETTER_TYPE_DELAY = 0.01
    LINE_TYPE_DELAY   = 3.5

    def __init__(self, rules_file, activator_key):
        self.rules = []
        self._load_rules(rules_file)

        self.keyboard_ctrl = keyboard.Controller()
        self.activator_key = activator_key
        self.listener = None


    def _type_key(self, key):
        self.keyboard_ctrl.press(key)
        self.keyboard_ctrl.release(key)


    def _type_phrase(self, phrase, delay=0.0):
        for letter in phrase:
            self._type_key(letter)
            time.sleep(delay)


    def _load_rules(self, file_loc):
        with open(file_loc, 'r') as fp:
            # NOTE: We don't want to type empty lines so we call strip() twice due to list comprehension logic
            self.rules = [line.strip() for line in fp.readlines() if len(line.strip()) > 0]


    # Only type the rules once, otherwise ignore the signal (via the throttle)
    @throttle(30.0)
    def _type_rules(self):
        print('Typing rules...')

        # Pause for 1 second before typing the rules
        time.sleep(1.0)

        for line in self.rules:
            # Type each line and send an enter key
            self._type_phrase(line, delay=self.LETTER_TYPE_DELAY)
            self._type_key(keyboard.Key.enter)
            time.sleep(self.LINE_TYPE_DELAY)


    def start(self):
        if self.listener is None or not self.listener.running:
            # NOTE: When a thread is started and stopped, a new one must be instantiated
            self.listener = keyboard.GlobalHotKeys({
                self.activator_key: self._type_rules
            })

            self.listener.start()
            self.listener.wait()
            print(f'Listener started! Press "{self.activator_key}" to blast the rules. Press Ctrl+C to stop this service.')


    def stop(self):
        if self.listener is not None and self.listener.running:
            self.listener.stop()

        self.listener = None
        print('Listener stopped!')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: Please specify the path to the rules file')
        exit(1)

    rules_path = sys.argv[1]
    if not os.path.exists(rules_path):
        print('Error: The path to the rules file does not exist')
        exit(1)

    service = RulesBlasterService(
        rules_file=rules_path,
        activator_key='<ctrl>+1'
    )

    service.start()
    running = True

    while running:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            running = False

    service.stop()
