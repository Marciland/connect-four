'''Networking.'''
from queue import Queue
from socket import AF_INET, SOCK_STREAM, socket, timeout
from threading import Event, Thread
from typing import TYPE_CHECKING

from assets import MultiplayerCancelMessage, MultiplayerMessage

if TYPE_CHECKING:
    from components import MainWindow


class Communication:
    '''Handles in and out.'''

    def __init__(self, window) -> None:
        self.window: MainWindow = window
        self._port = 51231
        self._connected_event = Event()
        self._connection: socket = None

    def connection_established(self) -> bool:
        '''Wait for an incoming connection.'''
        Thread(target=self._wait_for_connection,
               daemon=True).start()
        title = self.window.translation.get('multiplayer_host')
        msg = self.window.translation.get('multiplayer_host_msg')
        message = MultiplayerCancelMessage(frame=self.window.current_frame,
                                           event=self._connected_event,
                                           title=title,
                                           msg=msg)
        if message.canceled:
            return False
        return True

    def _wait_for_connection(self) -> None:
        server_socket = socket(family=AF_INET, type=SOCK_STREAM)
        server_socket.bind(('0.0.0.0', self._port))
        server_socket.listen()
        server_socket.settimeout(0.1)
        while not self._connected_event.is_set():
            try:
                con, _ = server_socket.accept()
                self._connection = con
            except timeout:
                continue
            self._connected_event.set()
        server_socket.close()

    def get_move(self) -> int:
        '''Waits for the next move.'''
        receiving_event = Event()
        received_move = Queue(maxsize=1)
        Thread(target=self._get_move,
               args=[received_move, receiving_event],
               daemon=True).start()
        title = self.window.translation.get('multiplayer_get_move')
        msg = self.window.translation.get('multiplayer_get_move_msg')
        MultiplayerMessage(frame=self.window.current_frame,
                           event=receiving_event,
                           title=title,
                           msg=msg)
        return received_move.get()

    def _get_move(self, queue: Queue, event: Event) -> None:
        while not event.is_set():
            data = self._connection.recv(1)
            if len(data) == 1:
                move = data.decode(encoding='utf-8')
                queue.put(int(move))
                event.set()

    def send_move(self, move: int) -> None:
        '''Makes a move.'''
        data = str(move).encode(encoding='utf-8')
        self._connection.send(data)

    def joined_game(self, ip: str) -> bool:
        '''Join a game.'''
        Thread(target=self._join_game,
               args=[ip],
               daemon=True).start()
        title = self.window.translation.get('multiplayer_join')
        msg = self.window.translation.get('multiplayer_join_msg')
        message = MultiplayerCancelMessage(frame=self.window.current_frame,
                                           event=self._connected_event,
                                           title=title,
                                           msg=msg)
        if message.canceled:
            self._connection.close()
            return False
        return True

    def _join_game(self, ip: str) -> None:
        while not self._connected_event.is_set():
            self._connection = socket(family=AF_INET, type=SOCK_STREAM)
            self._connection.settimeout(0.1)
            try:
                self._connection.connect((ip, self._port))
            except timeout:
                continue
            except OSError as ex:
                # 10038 happens if socket is closed from main thread before this thread is stopped
                if '10038' in str(ex):
                    break
            self._connection.settimeout(None)
            self._connected_event.set()
