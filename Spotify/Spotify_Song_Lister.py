import sys, os
import spotipy
import spotipy.util as util
import pyperclip

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(
    username,
    scope,
    client_id='07d747a4c3cf4b1db3338cc31a3d5e0b',
    client_secret='f540ed7dc884437bafc100635eb86c21',
    redirect_uri='https://open.spotify.com/'
)
if token:
    #pip install pyperclip
    sp = spotipy.Spotify(auth=token)
    for i in range(-120,0):
        results = sp.current_user_saved_tracks(limit=1, offset=-i)
        for item in results['items']:
            track = item['track']
            print ("Copied " + track['name'] + ' - ' + track['artists'][0]['name'])
            pyperclip.copy(track['name'] + ' - ' + track['artists'][0]['name'])
            input("Press Enter to continue...")
else:
    print ("Can't get token for", username)