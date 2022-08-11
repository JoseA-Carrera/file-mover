import os

# your Computer path
downloads_folder = r'/home/swapps/Descargas/'
pictures_folder = r'/home/swapps/Imágenes/'
music_folder = r'/home/swapps/Música/'
documents_folder = r'/home/swapps/Documentos/'
videos_folder = r'/home/swapps/Vídeos/'


if __name__ == '__main__':
    # iterate each element of downloads_folder
    for filename in os.listdir(downloads_folder):
        # separate by name and extension each file
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in ['.jpg', '.jpeg', '.png']:
            os.rename(downloads_folder + filename, pictures_folder + filename)
            print(f'file {filename} to {pictures_folder}')

        if extension in ['.mp3']:
            os.rename(downloads_folder + filename, music_folder + filename)
            print(f'file {filename} to {music_folder}')

        if extension in ['.pdf']:
            os.rename(downloads_folder + filename, documents_folder + filename)
            print(f'file {filename} to {documents_folder}')

        if extension in ['.mp4']:
            os.rename(downloads_folder + filename, videos_folder + filename)
            print(f'file {filename} to {documents_folder}')
