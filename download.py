from pytube import YouTube

# this is youtube downloader
url = input('what is the url? ')
yt = YouTube(url=url)
print
d  = yt.streams.get_by_resolution(resolution='720p')
print(f'{d.title} downloading .....')
d.download()
print('finished downloading !!!!')
