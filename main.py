import instaloader

instagram = instaloader.Instaloader()
profil = input("Username: ")
instagram.download_profile(profil,profile_pic_only=True)