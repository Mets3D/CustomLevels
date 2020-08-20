import json

# This script generates a playlist out of all ranked maps between a given star rating range.

# File that contains scrapped map data downloaded from https://github.com/andruzzzhka/BeatSaberScrappedData
scrapped_data_file = "D:\\Met-PC\\Desktop\\combinedScrappedData.json" 

min_star = 6.0
max_star = 7.0
playlist_name = "6-7 Star Ranked"
ranked = True

# File where the filtered and sorted playlist is outputted.
playlist_file = f"D:\\Met-PC\\Desktop\\{playlist_name}.json"

def load_json(file):
	with open(scrapped_data_file, encoding='utf-8') as json_file:
		return json.load(json_file)

def write_json(data, filepath):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		json.dump(data, outfile, indent=2)

def get_rated_maps(ranked=False):
	scrapped_data = load_json(scrapped_data_file)
	rated_maps = []
	for map_info in scrapped_data:
		for diff in map_info["Diffs"]:
			if diff["Stars"]>0:
				if ranked and diff["Ranked"]:
					break
				rated_maps.append(map_info)
				break

	return rated_maps

# Filter ranked maps
rated_maps = get_rated_maps()

# Filter and sort maps by star rating
filtered_maps = []
for map_info in rated_maps:
	for diff in map_info["Diffs"]:
		if ranked and not diff["Ranked"]: continue
		if min_star < diff["Stars"] < max_star:
			if map_info in filtered_maps:
				if diff["Stars"] > map_info["highest_star_rating_in_filter_range"]:
					map_info["highest_star_rating_in_filter_range"] = diff["Stars"]
			else:
				map_info["highest_star_rating_in_filter_range"] = diff["Stars"]		
				filtered_maps.append(map_info)

# Sort maps by star rating.
sorted_maps = sorted(filtered_maps, key=lambda beatmap: beatmap["highest_star_rating_in_filter_range"])

playlist_songs = []

for beatmap in sorted_maps:
	playlist_song_data = {}
	playlist_song_data["hash"] = beatmap["Hash"]
	playlist_song_data["songName"] = beatmap["SongName"]
	playlist_songs.append(playlist_song_data)

playlist_data = {
"playlistTitle":playlist_name,
"playlistAuthor":"Mets",
"image":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC+aJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIeSURBVGhD7Zm9kcIwEEYVMQ4JCSmDkDIogZAuKIGQMiiNkNsZfWgW7P0sy8iCm33BDfpb7ZMlY87h8eO4QGtcoDUu0BoXaM3/Fbjdbvv9/nq9ojyPz0bTmAKbzSaE0HUdyq9IQtvtVjrI35y0UrQ0UJMZZBBTALFDiKEHJ9aQJGQsOoUQTfqIW5mDKSARY+jVasVTT1iXSyedwvYpczAFzuczAtvsdjt8eiKjMF6BthCOx2MMKx/Q9jqRtQQEdogRVaEn1pxOp9hhMIPYJKDcQzsMLgHBDPq2bazUI/f7Hf2GskSDLSDwJSBkrQqqbPTlQpUCDTQOXwIC6414GRH1MUWVAg1jcdBpeYHL5YJ+xk5D23cKyOZZr9ex2+FwQK1C66HKAJ2WFNDZC7KP0aBIu2tQL8FPEaFQQObLvE2h2dCLvC0EavMoEZDvSz2fQG6y6PF8JOnzlj2/X/eZINBf9QifEp2GnhTyLyMhS8B6FsqZD10zKMheyBLoIyeS7OmErDEGjFGWvTBZYNJM1sOzpjj1yIQzUADGz86SsJAAyhVwAQrGuwDBBSgY7wIEF6BgvAsQXICC8S5AqCigfwygqgIVBfh/uz5FRQEMrvljQFhCAOU6uIANBv+uQPd8m4RyHVj0lMHUtyaR+Iah6gkWmEDxW5MlYQLFb02WZCSzZfbxHEYyW2Yfz+F7lzYTF2iNC7TGBVrjAq35cYHH4w8+O0nkg6AjAwAAAABJRU5ErkJggg==",
"songs": playlist_songs
}

write_json(playlist_data, playlist_file)