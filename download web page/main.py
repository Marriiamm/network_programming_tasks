import socket
import tkinter as tk
import threading


class PageDownload:

    def __init__(self, url):
        self.url = url
        self.host = self.get_host()
        self.path = self.get_path()

    def get_host(self):
        return self.url.split('/')[2]

    def get_path(self):
        return '/' + '/'.join(self.url.split('/')[3:])

    def download(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to {self.host}...")
        s.connect((self.host, 80))
        print(f"Connected to {self.host}.")

        request = f"GET {self.path} HTTP/1.1\r\nHost: {self.host}\r\nAccept:text/html\r\n\r\n"
        s.send(request.encode())

        response = ''
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data.decode('utf-8', errors='replace')

        s.close()

        try:
            with open("C:/Users/Dell/Desktop/webpage.html", "w", encoding="utf-8") as f:
                content = response.split('\r\n\r\n')[1]
                print(f"Writing {len(content)} to file...")
                f.write(content)
                print("mission done successfully!")
        except Exception as e:
            print(f"Error writing file: {e}")


class gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.root.title("Page Downloader")

        self.url_label = tk.Label(self.root, text="Enter URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self.root)
        self.url_entry.pack()

        self.download_button = tk.Button(self.root, text="Download", command=self.download)
        self.download_button.pack()

        self.root.mainloop()

    def download(self):
        url = self.url_entry.get()
        downloader = PageDownload(url)
        t = threading.Thread(target=downloader.download)
        t.start()


if __name__ == "__main__":
    gui = gui()
