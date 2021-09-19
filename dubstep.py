def song_decoder(song):
    dec_song = song.replace('WUB', ' ').strip()
    return ' '.join(dec_song.split())

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
