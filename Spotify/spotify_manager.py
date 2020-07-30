import sys
import spotipy
import webbrowser
import spotipy.util as util
from sys import exit

scope = 'user-library-read'
global token

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def setup(username):
    global token
    try:
        token = util.prompt_for_user_token(
            username,
            scope,
            client_id='07d747a4c3cf4b1db3338cc31a3d5e0b',
            client_secret='f540ed7dc884437bafc100635eb86c21',
            redirect_uri='https://open.spotify.com/'
        )
    except spotipy.oauth2.SpotifyOauthError as e:
        if "Bad Request" in str(e):
            print("Failed to authenticate user")
            return 1

    if token:
        print("Successfully setup spotify user")
        return 0
    else:
        print ("Can't get token for", username)
        return 1

if __name__ == "__main__":

    username = sys.argv[2]

    if sys.argv[1] == "setup": 
        setup(username)
    
    elif sys.argv[1] == 'songsearch':
        token = util.prompt_for_user_token(
        	username,
        	scope,
        	client_id='07d747a4c3cf4b1db3338cc31a3d5e0b',
        	client_secret='f540ed7dc884437bafc100635eb86c21',
        	redirect_uri='https://open.spotify.com/'
        )

        if token:
            sp = spotipy.Spotify(auth=token)
            if len(sys.argv) == 6:
                artist = sys.argv[3]
                track = sys.argv[4]
                browser = sys.argv[5].replace("\\", "/")
            else:
                artist = input("Enter artist name: ")
                track = input("Enter the track name: ")
                browser = input("Enter the location of your browser: ")

            track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
            # print(track_id['tracks']['items'])
            if len(track_id['tracks']['items'])  == 0:
            	print("No tracks found.\nCheck your query for spelling errors if u think this is a mistake")
            else:
                # webbrowser.get(browser + " %s").open(track_id['tracks']['items'][0]['external_urls']['spotify'])
                webbrowser.get(browser + " %s").open(track_id['tracks']['items'][0]['external_urls']['spotify'])

        else:
            print ("Can't get token for", username)