class TextEditor:
    def __init__(self):
        self.content = ''  # type: ignore
        self.undo_stack = []  # type: ignore

    def write(self, teks):
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'Tulis: {self.content}')

    def undo(self):
        if self.undo_stack:  # type: ignore # ada riwayat?
            # Kembalikan ke state sebelumnya
            self.content = self.undo_stack.pop()  # type: ignore
            print(f'UNDO → {self.content}')  # type: ignore
        else:
            print('Tidak bisa undo lagi!')
editor = TextEditor()
editor.write('Halo') # content: 'Halo'
editor.write(' Dunia') # content: 'Halo Dunia'
editor.write('!') # content: 'Halo Dunia!'
editor.undo() # UNDO → 'Halo Dunia'
editor.undo() # UNDO → 'Halo'