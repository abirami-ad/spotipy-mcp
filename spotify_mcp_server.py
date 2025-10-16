from typing import Dict, Optional, Any, List
import spotipy
from fastmcp import FastMCP

mcp = FastMCP("Spotipy MCP Server")

def get_spotify_client(token: str) -> spotipy.Spotify:
    return spotipy.Spotify(auth=token)

@mcp.tool()
def get_album_info(token: str, album_id: str, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a single album given the album's ID, URIs or URL.

    Args:
        token: Spotify user token
        album_id: The album ID, URI or URL

    Returns:
        Dictionary containing detailed album information
    """
    try:
        spotify = get_spotify_client(token)
        album = spotify.album(album_id, market=market)
        return album

    except Exception as e:
        return {"error": f"Failed to get album info: {str(e)}"}

@mcp.tool()
def get_album_tracks(token: str, album_id: str, limit: int = 50, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Get Spotify catalog information about an album's tracks.

    Args:
        token: Spotify user token
        album_id: The album ID, URI or URL
        limit: The number of items to return
        offset: The index of the first item to return

    Returns:
        Dictionary containing album tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.album_tracks(album_id, limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get album tracks: {str(e)}"}

@mcp.tool()
def get_albums(token: str, albums: List[str], market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a list of albums given the album IDs, URIs, or URLs.

    Args:
        token: Spotify user token
        album_ids: A list of album IDs, URIs or URLs
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing album information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.albums(albums, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get albums: {str(e)}"}

@mcp.tool()
def get_artist_info(token: str, artist_id: str) -> Dict[str, Any]:
    """
    Returns a single artist given the artist's ID, URI or URL.

    Args:
        token: Spotify user token
        artist_id: An artist ID, URI or URL

    Returns:
        Dictionary containing detailed artist information
    """
    try:
        spotify = get_spotify_client(token)
        artist = spotify.artist(artist_id)
        return artist

    except Exception as e:
        return {"error": f"Failed to get artist info: {str(e)}"}

@mcp.tool()
def get_artist_albums(token: str, artist_id: str, album_type: Optional[str] = None, include_groups: Optional[str] = None, country: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get Spotify catalog information about an artist's albums.

    Args:
        token: Spotify user token
        artist_id: The artist ID, URI or URL
        album_type: The types of items to return. One or more of 'album', 'single', 'appears_on', 'compilation'
        limit: The number of albums to return
        offset: The index of the first album to return

    Returns:
        Dictionary containing artist's albums
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.artist_albums(artist_id, album_type=album_type, include_groups=include_groups, country=country, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get artist albums: {str(e)}"}

@mcp.tool()
def get_artist_related_artists(token: str, artist_id: str) -> Dict[str, Any]:
    """
    Get Spotify catalog information about artists similar to an identified artist. Similarity is based on analysis of the Spotify community's listening history.

    Args:
        token: Spotify user token
        artist_id: The artist ID, URI or URL

    Returns:
        Dictionary containing related artists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.artist_related_artists(artist_id)
        return results

    except Exception as e:
        return {"error": f"Failed to get related artists: {str(e)}"}

@mcp.tool()
def get_artist_top_tracks(token: str, artist_id: str, country: str = "US") -> Dict[str, Any]:
    """
    Get Spotify catalog information about an artist's top 10 tracks by country.

    Args:
        token: Spotify user token
        artist_id: The artist ID, URI or URL
        country: Limit the response to one particular country

    Returns:
        Dictionary containing artist's top tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.artist_top_tracks(artist_id, country=country)
        return results

    except Exception as e:
        return {"error": f"Failed to get artist top tracks: {str(e)}"}

@mcp.tool()
def get_artists(token: str, artists: List[str]) -> Dict[str, Any]:
    """
    Returns a list of artists given the artist IDs, URIs, or URLs.

    Args:
        token: Spotify user token
        artist_ids: A list of artist IDs, URIs or URLs

    Returns:
        Dictionary containing artist information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.artists(artists)
        return results

    except Exception as e:
        return {"error": f"Failed to get artists: {str(e)}"}

@mcp.tool()
def get_audio_analysis(token: str, track_id: str) -> Dict[str, Any]:
    """
    Get audio analysis for a track based upon its Spotify ID.

    Args:
        token: Spotify user token
        track_id: A track URI, URL or ID

    Returns:
        Dictionary containing detailed audio analysis
    """
    try:
        spotify = get_spotify_client(token)
        analysis = spotify.audio_analysis(track_id)
        return analysis

    except Exception as e:
        return {"error": f"Failed to get audio analysis: {str(e)}"}

@mcp.tool()
def get_audio_features(token: str, tracks: List[str]) -> Dict[str, Any]:
    """
    Get audio features for one or multiple tracks based upon their Spotify IDs.

    Args:
        token: Spotify user token
        track_id: A list of track URIs, URLs or IDs, maximum: 100 ids

    Returns:
        Dictionary containing audio features
    """
    try:
        spotify = get_spotify_client(token)
        features = spotify.audio_features(tracks)
        return features if features else {"audio_features": None}

    except Exception as e:
        return {"error": f"Failed to get audio features: {str(e)}"}

@mcp.tool()
def get_available_markets(token: str) -> Dict[str, Any]:
    """    Get the list of markets where Spotify is available. Returns a list of the countries in which Spotify is available, identified by their ISO 3166-1 alpha-2 country code with additional country codes for special territories.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing available markets
    """
    try:
        spotify = get_spotify_client(token)
        markets = spotify.available_markets()
        return markets

    except Exception as e:
        return {"error": f"Failed to get available markets: {str(e)}"}

@mcp.tool()
def get_categories(token: str, country: Optional[str] = None, locale: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of categories.

    Args:
        token: Spotify user token
        country: An ISO 3166-1 alpha-2 country code
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
        offset: The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items

    Returns:
        Dictionary containing browse categories
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.categories(country=country, locale=locale, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get categories: {str(e)}"}

@mcp.tool()
def get_category(token: str, category_id: str, country: Optional[str] = None, locale: Optional[str] = None) -> Dict[str, Any]:
    """
    Get info about a category.

    Args:
        token: Spotify user token
        category_id: The Spotify category ID for the category
        country: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing category information
    """
    try:
        spotify = get_spotify_client(token)
        category = spotify.category(category_id, country=country, locale=locale)
        return category

    except Exception as e:
        return {"error": f"Failed to get category: {str(e)}"}

@mcp.tool()
def get_category_playlists(token: str, category_id: str, country: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of playlists for a specific Spotify category.

    Args:
        token: Spotify user token
        category_id: The Spotify category ID for the category
        country: An ISO 3166-1 alpha-2 country code
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
        offset: The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items

    Returns:
        Dictionary containing category playlists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.category_playlists(category_id, country=country, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get category playlists: {str(e)}"}

@mcp.tool()
def get_episode(token: str, episode_id: str, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a single episode given the episode's ID, URIs or URL.

    Args:
        token: Spotify user token
        episode_id: The episode ID, URI or URL
        market: An ISO 3166-1 alpha-2 country code. The episode must be available in the given market

    Returns:
        Dictionary containing episode information
    """
    try:
        spotify = get_spotify_client(token)
        episode = spotify.episode(episode_id, market=market)
        return episode

    except Exception as e:
        return {"error": f"Failed to get episode: {str(e)}"}

@mcp.tool()
def get_episodes(token: str, ids: List[str], market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a list of episodes given the episode IDs, URIs, or URLs.

    Args:
        token: Spotify user token
        episode_ids: A list of episode IDs, URIs or URLs
        market: An ISO 3166-1 alpha-2 country code. Only episodes available in the given market will be returned

    Returns:
        Dictionary containing episode information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.episodes(ids, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get episodes: {str(e)}"}

@mcp.tool()
def get_featured_playlists(token: str, locale: Optional[str] = None, country: Optional[str] = None, timestamp: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of Spotify featured playlists.

    Args:
        token: Spotify user token
        country: An ISO 3166-1 alpha-2 country code
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
        offset: The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items

    Returns:
        Dictionary containing featured playlists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.featured_playlists(locale=locale, country=country, timestamp=timestamp, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get featured playlists: {str(e)}"}

@mcp.tool()
def get_audiobook(token: str, id: str, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Get Spotify catalog information for a single audiobook identified by its unique Spotify ID.

    Args:
        token: Spotify user token
        audiobook_id: The Spotify ID for the audiobook
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing audiobook information
    """
    try:
        spotify = get_spotify_client(token)
        audiobook = spotify.get_audiobook(id, market=market)
        return audiobook

    except Exception as e:
        return {"error": f"Failed to get audiobook: {str(e)}"}

@mcp.tool()
def get_audiobook_chapters(token: str, id: str, market: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get Spotify catalog information about an audiobook's chapters.

    Args:
        token: Spotify user token
        audiobook_id: The Spotify ID for the audiobook
        limit: The maximum number of items to return
        offset: The index of the first item to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing audiobook chapters
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.get_audiobook_chapters(id, market=market, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get audiobook chapters: {str(e)}"}

@mcp.tool()
def get_audiobooks(token: str, ids: List[str], market: Optional[str] = None) -> Dict[str, Any]:
    """
    Get Spotify catalog information for multiple audiobooks based on their Spotify IDs.

    Args:
        token: Spotify user token
        audiobook_ids: A list of Spotify IDs for the audiobooks
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing audiobook information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.get_audiobooks(ids, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get audiobooks: {str(e)}"}

@mcp.tool()
def get_new_releases(token: str, country: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of new album releases featured in Spotify.

    Args:
        token: Spotify user token
        country: An ISO 3166-1 alpha-2 country code
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
        offset: The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items

    Returns:
        Dictionary containing new album releases
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.new_releases(country=country, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get new releases: {str(e)}"}

@mcp.tool()
def get_playlist_info(token: str, playlist_id: str) -> Dict[str, Any]:
    """
    Gets playlist by id.

    Args:
        token: Spotify user token
        playlist_id: The id of the playlist

    Returns:
        Dictionary containing detailed playlist information
    """
    try:
        spotify = get_spotify_client(token)
        playlist = spotify.playlist(playlist_id)
        return playlist

    except Exception as e:
        return {"error": f"Failed to get playlist info: {str(e)}"}

@mcp.tool()
def get_playlist_tracks(token: str, playlist_id: str, fields: Optional[str] = None, limit: int = 100, offset: int = 0, market: Optional[str] = None, additional_types: Optional[str] = None) -> Dict[str, Any]:
    """
    Get full details of the tracks of a playlist.

    Args:
        token: Spotify user token
        playlist_id: The playlist ID, URI or URL
        limit: The maximum number of tracks to return
        offset: The index of the first track to return

    Returns:
        Dictionary containing playlist tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.playlist_tracks(playlist_id, fields=fields, limit=limit, offset=offset, market=market, additional_types=additional_types)
        return results

    except Exception as e:
        return {"error": f"Failed to get playlist tracks: {str(e)}"}

@mcp.tool()
def playlist_cover_image(token: str, playlist_id: str) -> Dict[str, Any]:
    """
    Get cover image of a playlist.

    Args:
        token: Spotify user token
        playlist_id: The playlist ID, URI or URL

    Returns:
        Dictionary containing playlist cover image information
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.playlist_cover_image(playlist_id)
        return {"images": result}

    except Exception as e:
        return {"error": f"Failed to get playlist cover image: {str(e)}"}

@mcp.tool()
def playlist_is_following(token: str, playlist_id: str, user_ids: List[str]) -> Dict[str, Any]:
    """
    Check if users follow playlist.

    Args:
        token: Spotify user token
        playlist_id: The playlist ID, URI or URL
        user_ids: A list of user IDs to check

    Returns:
        Dictionary containing following status for each user
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.playlist_is_following(playlist_id, user_ids)
        return {"following": result}

    except Exception as e:
        return {"error": f"Failed to check playlist following status: {str(e)}"}

@mcp.tool()
def get_available_genres(token: str) -> Dict[str, Any]:
    """
    Get available genres for recommendations.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing available genres
    """
    try:
        spotify = get_spotify_client(token)
        genres = spotify.recommendation_genre_seeds()
        return genres

    except Exception as e:
        return {"error": f"Failed to get available genres: {str(e)}"}

@mcp.tool()
def get_recommendations(token: str, seed_artists: Optional[List[str]] = None, seed_genres: Optional[List[str]] = None,
                      seed_tracks: Optional[List[str]] = None, limit: int = 20, market: Optional[str] = None,
                      min_acousticness: Optional[float] = None, max_acousticness: Optional[float] = None, target_acousticness: Optional[float] = None,
                      min_danceability: Optional[float] = None, max_danceability: Optional[float] = None, target_danceability: Optional[float] = None,
                      min_duration_ms: Optional[int] = None, max_duration_ms: Optional[int] = None, target_duration_ms: Optional[int] = None,
                      min_energy: Optional[float] = None, max_energy: Optional[float] = None, target_energy: Optional[float] = None,
                      min_instrumentalness: Optional[float] = None, max_instrumentalness: Optional[float] = None, target_instrumentalness: Optional[float] = None,
                      min_key: Optional[int] = None, max_key: Optional[int] = None, target_key: Optional[int] = None,
                      min_liveness: Optional[float] = None, max_liveness: Optional[float] = None, target_liveness: Optional[float] = None,
                      min_loudness: Optional[float] = None, max_loudness: Optional[float] = None, target_loudness: Optional[float] = None,
                      min_mode: Optional[int] = None, max_mode: Optional[int] = None, target_mode: Optional[int] = None,
                      min_popularity: Optional[int] = None, max_popularity: Optional[int] = None, target_popularity: Optional[int] = None,
                      min_speechiness: Optional[float] = None, max_speechiness: Optional[float] = None, target_speechiness: Optional[float] = None,
                      min_tempo: Optional[float] = None, max_tempo: Optional[float] = None, target_tempo: Optional[float] = None,
                      min_time_signature: Optional[int] = None, max_time_signature: Optional[int] = None, target_time_signature: Optional[int] = None,
                      min_valence: Optional[float] = None, max_valence: Optional[float] = None, target_valence: Optional[float] = None) -> Dict[str, Any]:
    """
    Get a list of recommended tracks for one to five seeds. (at least one of seed_artists, seed_tracks and seed_genres are needed)

    Args:
        token: Spotify user token
        seed_artists: A list of artist IDs, URIs or URLs
        seed_genres: A list of genre names. Available genres for recommendations can be found by calling recommendation_genre_seeds
        seed_tracks: A list of track IDs, URIs or URLs
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 100
        target_danceability: Target danceability (0.0-1.0)
        target_energy: Target energy (0.0-1.0)
        target_valence: Target valence (0.0-1.0)
        target_tempo: Target tempo (BPM)

    Returns:
        Dictionary containing recommended tracks
    """
    try:
        spotify = get_spotify_client(token)

        results = spotify.recommendations(
            seed_artists=seed_artists,
            seed_genres=seed_genres,
            seed_tracks=seed_tracks,
            limit=limit,
            market=market,
            min_acousticness=min_acousticness,
            max_acousticness=max_acousticness,
            target_acousticness=target_acousticness,
            min_danceability=min_danceability,
            max_danceability=max_danceability,
            target_danceability=target_danceability,
            min_duration_ms=min_duration_ms,
            max_duration_ms=max_duration_ms,
            target_duration_ms=target_duration_ms,
            min_energy=min_energy,
            max_energy=max_energy,
            target_energy=target_energy,
            min_instrumentalness=min_instrumentalness,
            max_instrumentalness=max_instrumentalness,
            target_instrumentalness=target_instrumentalness,
            min_key=min_key,
            max_key=max_key,
            target_key=target_key,
            min_liveness=min_liveness,
            max_liveness=max_liveness,
            target_liveness=target_liveness,
            min_loudness=min_loudness,
            max_loudness=max_loudness,
            target_loudness=target_loudness,
            min_mode=min_mode,
            max_mode=max_mode,
            target_mode=target_mode,
            min_popularity=min_popularity,
            max_popularity=max_popularity,
            target_popularity=target_popularity,
            min_speechiness=min_speechiness,
            max_speechiness=max_speechiness,
            target_speechiness=target_speechiness,
            min_tempo=min_tempo,
            max_tempo=max_tempo,
            target_tempo=target_tempo,
            min_time_signature=min_time_signature,
            max_time_signature=max_time_signature,
            target_time_signature=target_time_signature,
            min_valence=min_valence,
            max_valence=max_valence,
            target_valence=target_valence
        )
        return results

    except Exception as e:
        return {"error": f"Failed to get recommendations: {str(e)}"}

@mcp.tool()
def search_tracks(token: str, query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Searches for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response
        offset: The index of the first item to return

    Returns:
        Dictionary containing search results with track information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search(q=query, type="track", limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Track search failed: {str(e)}"}

@mcp.tool()
def search_artists(token: str, query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Searches for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response
        offset: The index of the first item to return

    Returns:
        Dictionary containing search results with artist information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search(q=query, type="artist", limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Artist search failed: {str(e)}"}

@mcp.tool()
def search_albums(token: str, query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Searches for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response
        offset: The index of the first item to return

    Returns:
        Dictionary containing search results with album information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search(q=query, type="album", limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Album search failed: {str(e)}"}

@mcp.tool()
def search_playlists(token: str, query: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """
    Searches for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response
        offset: The index of the first item to return

    Returns:
        Dictionary containing search results with playlist information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search(q=query, type="playlist", limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Playlist search failed: {str(e)}"}

@mcp.tool()
def get_show(token: str, show_id: str, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a single show given the show's ID, URIs or URL.

    Args:
        token: Spotify user token
        show_id: The show ID, URI or URL
        market: An ISO 3166-1 alpha-2 country code. The show must be available in the given market

    Returns:
        Dictionary containing show information
    """
    try:
        spotify = get_spotify_client(token)
        show = spotify.show(show_id, market=market)
        return show

    except Exception as e:
        return {"error": f"Failed to get show: {str(e)}"}

@mcp.tool()
def get_show_episodes(token: str, show_id: str, limit: int = 50, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Get Spotify catalog information about a show's episodes.

    Args:
        token: Spotify user token
        show_id: The show ID, URI or URL
        limit: The number of items to return
        offset: The index of the first item to return
        market: An ISO 3166-1 alpha-2 country code. Only episodes available in the given market will be returned

    Returns:
        Dictionary containing show episodes
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.show_episodes(show_id, limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get show episodes: {str(e)}"}

@mcp.tool()
def get_shows(token: str, ids: List[str], market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a list of shows given the show IDs, URIs, or URLs.

    Args:
        token: Spotify user token
        ids: A list of show IDs, URIs or URLs
        market: An ISO 3166-1 alpha-2 country code. Only shows available in the given market will be returned

    Returns:
        Dictionary containing show information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.shows(ids, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get shows: {str(e)}"}

@mcp.tool()
def get_track_info(token: str, track_id: str) -> Dict[str, Any]:
    """
    Returns a single track given the track's ID, URI or URL.

    Args:
        token: Spotify user token
        track_id: A spotify URI, URL or ID

    Returns:
        Dictionary containing detailed track information
    """
    try:
        spotify = get_spotify_client(token)
        track = spotify.track(track_id)
        return track

    except Exception as e:
        return {"error": f"Failed to get track info: {str(e)}"}

@mcp.tool()
def get_tracks(token: str, ids: List[str], market: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a list of tracks given a list of track IDs, URIs, or URLs.

    Args:
        token: Spotify user token
        ids: A list of spotify URIs, URLs or IDs. Maximum: 50 IDs
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing track information
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.tracks(ids, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get tracks: {str(e)}"}

@mcp.tool()
def get_user(token: str, user_id: str) -> Dict[str, Any]:
    """
    Gets basic profile information about a Spotify User.

    Args:
        token: Spotify user token
        user_id: The id of the user

    Returns:
        Dictionary containing user profile information
    """
    try:
        spotify = get_spotify_client(token)
        user = spotify.user(user_id)
        return user

    except Exception as e:
        return {"error": f"Failed to get user: {str(e)}"}

@mcp.tool()
def get_user_playlists(token: str, user_id: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """
    Gets playlists of a user.

    Args:
        token: Spotify user token
        user_id: The id of the user
        limit: The number of items to return
        offset: The index of the first item to return

    Returns:
        Dictionary containing user's playlists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.user_playlists(user_id, limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get user playlists: {str(e)}"}

@mcp.tool()
def get_current_playback(token: str, market: Optional[str] = None, additional_types: Optional[str] = None) -> Dict[str, Any]:
    """
    Get information about user's current playback.

    Args:
        token: Spotify user token
        market: An ISO 3166-1 alpha-2 country code
        additional_types: Episode to get podcast track information

    Returns:
        Dictionary containing current playback information
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_playback(market=market, additional_types=additional_types)
        return result if result else {"playback": None}

    except Exception as e:
        return {"error": f"Failed to get current playback: {str(e)}"}

@mcp.tool()
def get_current_user(token: str) -> Dict[str, Any]:
    """
    Get detailed profile information about the current user.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing current user profile information
    """
    try:
        spotify = get_spotify_client(token)
        user = spotify.current_user()
        return user

    except Exception as e:
        return {"error": f"Failed to get current user: {str(e)}"}

@mcp.tool()
def get_current_user_followed_artists(token: str, limit: int = 20, after: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a list of the artists followed by the current authorized user.

    Args:
        token: Spotify user token
        limit: The number of artists to return
        after: The last artist ID retrieved from the previous request

    Returns:
        Dictionary containing followed artists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_followed_artists(limit=limit, after=after)
        return results

    except Exception as e:
        return {"error": f"Failed to get followed artists: {str(e)}"}

@mcp.tool()
def check_current_user_following_artists(token: str, ids: List[str]) -> Dict[str, Any]:
    """
    Check if the current user is following certain artists.

    Args:
        token: Spotify user token
        ids: A list of artist URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans respective to ids
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_following_artists(ids=ids)
        return {"following": result}

    except Exception as e:
        return {"error": f"Failed to check if following artists: {str(e)}"}

@mcp.tool()
def check_current_user_following_users(token: str, ids: List[str]) -> Dict[str, Any]:
    """
    Check if the current user is following certain users.

    Args:
        token: Spotify user token
        ids: A list of user URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans respective to ids
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_following_users(ids=ids)
        return {"following": result}

    except Exception as e:
        return {"error": f"Failed to check if following users: {str(e)}"}

@mcp.tool()
def get_current_user_playing_track(token: str) -> Dict[str, Any]:
    """
    Get information about the current users currently playing track.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing currently playing track information
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_playing_track()
        return result if result else {"track": None}

    except Exception as e:
        return {"error": f"Failed to get currently playing track: {str(e)}"}

@mcp.tool()
def get_current_user_playlists(token: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """
    Get current user playlists without required getting his profile.

    Args:
        token: Spotify user token
        limit: The number of items to return
        offset: The index of the first item to return

    Returns:
        Dictionary containing current user's playlists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_playlists(limit=limit, offset=offset)
        return results

    except Exception as e:
        return {"error": f"Failed to get current user playlists: {str(e)}"}

@mcp.tool()
def get_current_user_recently_played(token: str, limit: int = 50, after: Optional[int] = None, before: Optional[int] = None) -> Dict[str, Any]:
    """
    Get the current user's recently played tracks.

    Args:
        token: Spotify user token
        limit: The number of entities to return
        after: Unix timestamp in milliseconds. Returns all items after (but not including) this cursor position
        before: Unix timestamp in milliseconds. Returns all items before (but not including) this cursor position

    Returns:
        Dictionary containing recently played tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_recently_played(limit=limit, after=after, before=before)
        return results

    except Exception as e:
        return {"error": f"Failed to get recently played tracks: {str(e)}"}

@mcp.tool()
def get_current_user_saved_albums(token: str, limit: int = 20, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a list of the albums saved in the current authorized user's "Your Music" library.

    Args:
        token: Spotify user token
        limit: The number of albums to return (MAX_LIMIT=50)
        offset: The index of the first album to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing saved albums
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_saved_albums(limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get saved albums: {str(e)}"}

@mcp.tool()
def check_current_user_saved_albums(token: str, albums: List[str]) -> Dict[str, Any]:
    """
    Check if one or more albums is already saved in the current Spotify user's "Your Music" library.

    Args:
        token: Spotify user token
        albums: A list of album URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans indicating if albums are saved
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_saved_albums_contains(albums=albums)
        return {"saved": result}

    except Exception as e:
        return {"error": f"Failed to check saved albums: {str(e)}"}

@mcp.tool()
def get_current_user_saved_episodes(token: str, limit: int = 20, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a list of the episodes saved in the current authorized user's "Your Music" library.

    Args:
        token: Spotify user token
        limit: The number of episodes to return
        offset: The index of the first episode to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing saved episodes
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_saved_episodes(limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get saved episodes: {str(e)}"}

@mcp.tool()
def check_current_user_saved_episodes(token: str, episodes: List[str]) -> Dict[str, Any]:
    """
    Check if one or more episodes is already saved in the current Spotify user's "Your Music" library.

    Args:
        token: Spotify user token
        episodes: A list of episode URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans indicating if episodes are saved
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_saved_episodes_contains(episodes=episodes)
        return {"saved": result}

    except Exception as e:
        return {"error": f"Failed to check saved episodes: {str(e)}"}

@mcp.tool()
def get_current_user_saved_shows(token: str, limit: int = 20, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a list of the shows saved in the current authorized user's "Your Music" library.

    Args:
        token: Spotify user token
        limit: The number of shows to return
        offset: The index of the first show to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing saved shows
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_saved_shows(limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get saved shows: {str(e)}"}

@mcp.tool()
def check_current_user_saved_shows(token: str, shows: List[str]) -> Dict[str, Any]:
    """
    Check if one or more shows is already saved in the current Spotify user's "Your Music" library.

    Args:
        token: Spotify user token
        shows: A list of show URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans indicating if shows are saved
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_saved_shows_contains(shows=shows)
        return {"saved": result}

    except Exception as e:
        return {"error": f"Failed to check saved shows: {str(e)}"}

@mcp.tool()
def get_current_user_saved_tracks(token: str, limit: int = 20, offset: int = 0, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a list of the tracks saved in the current authorized user's "Your Music" library.

    Args:
        token: Spotify user token
        limit: The number of tracks to return
        offset: The index of the first track to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing saved tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_saved_tracks(limit=limit, offset=offset, market=market)
        return results

    except Exception as e:
        return {"error": f"Failed to get saved tracks: {str(e)}"}

@mcp.tool()
def check_current_user_saved_tracks(token: str, tracks: List[str]) -> Dict[str, Any]:
    """
    Check if one or more tracks is already saved in the current Spotify user's "Your Music" library.

    Args:
        token: Spotify user token
        tracks: A list of track URIs, URLs or IDs

    Returns:
        Dictionary containing list of booleans indicating if tracks are saved
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.current_user_saved_tracks_contains(tracks=tracks)
        return {"saved": result}

    except Exception as e:
        return {"error": f"Failed to check saved tracks: {str(e)}"}

@mcp.tool()
def get_current_user_top_artists(token: str, limit: int = 20, offset: int = 0, time_range: str = "medium_term") -> Dict[str, Any]:
    """
    Get the current user's top artists.

    Args:
        token: Spotify user token
        limit: The number of entities to return (max 50)
        offset: The index of the first entity to return
        time_range: Over what time frame are the affinities computed. Valid values: short_term, medium_term, long_term

    Returns:
        Dictionary containing top artists
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
        return results

    except Exception as e:
        return {"error": f"Failed to get top artists: {str(e)}"}

@mcp.tool()
def get_current_user_top_tracks(token: str, limit: int = 20, offset: int = 0, time_range: str = "medium_term") -> Dict[str, Any]:
    """
    Get the current user's top tracks.

    Args:
        token: Spotify user token
        limit: The number of entities to return
        offset: The index of the first entity to return
        time_range: Over what time frame are the affinities computed. Valid values: short_term, medium_term, long_term

    Returns:
        Dictionary containing top tracks
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.current_user_top_tracks(limit=limit, offset=offset, time_range=time_range)
        return results

    except Exception as e:
        return {"error": f"Failed to get top tracks: {str(e)}"}

@mcp.tool()
def get_currently_playing(token: str, market: Optional[str] = None, additional_types: Optional[str] = None) -> Dict[str, Any]:
    """
    Get user's currently playing track.

    Args:
        token: Spotify user token
        market: An ISO 3166-1 alpha-2 country code
        additional_types: Episode to get podcast track information

    Returns:
        Dictionary containing currently playing track information
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.currently_playing(market=market, additional_types=additional_types)
        return result if result else {"currently_playing": None}

    except Exception as e:
        return {"error": f"Failed to get currently playing: {str(e)}"}

@mcp.tool()
def get_devices(token: str) -> Dict[str, Any]:
    """
    Get a list of user's available devices.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing available devices
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.devices()
        return result

    except Exception as e:
        return {"error": f"Failed to get devices: {str(e)}"}

@mcp.tool()
def get_playlist_items(token: str, playlist_id: str, fields: Optional[str] = None, limit: int = 100, offset: int = 0, market: Optional[str] = None, additional_types: str = "track,episode") -> Dict[str, Any]:
    """
    Get full details of the tracks and episodes of a playlist.

    Args:
        token: Spotify user token
        playlist_id: The playlist ID, URI or URL
        fields: Which fields to return
        limit: The maximum number of tracks to return
        offset: The index of the first track to return
        market: An ISO 3166-1 alpha-2 country code
        additional_types: List of item types to return. Valid types are: track and episode

    Returns:
        Dictionary containing playlist items
    """
    try:
        spotify = get_spotify_client(token)
        additional_types_tuple = tuple(additional_types.split(",")) if additional_types else ("track", "episode")
        results = spotify.playlist_items(playlist_id, fields=fields, limit=limit, offset=offset, market=market, additional_types=additional_types_tuple)
        return results

    except Exception as e:
        return {"error": f"Failed to get playlist items: {str(e)}"}

@mcp.tool()
def get_queue(token: str) -> Dict[str, Any]:
    """
    Gets the current user's queue.

    Args:
        token: Spotify user token

    Returns:
        Dictionary containing user's queue
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.queue()
        return result

    except Exception as e:
        return {"error": f"Failed to get queue: {str(e)}"}

@mcp.tool()
def search_general(token: str, query: str, limit: int = 10, offset: int = 0, type: str = "track", market: Optional[str] = None) -> Dict[str, Any]:
    """
    Searches for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). The limit is applied within each type, not on the total response
        offset: The index of the first item to return
        type: The types of items to return. One or more of 'artist', 'album', 'track', 'playlist', 'show', and 'episode'. If multiple types are desired, pass in a comma separated string
        market: An ISO 3166-1 alpha-2 country code or the string from_token

    Returns:
        Dictionary containing search results
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search(q=query, limit=limit, offset=offset, type=type, market=market)
        return results

    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}

@mcp.tool()
def search_markets(token: str, query: str, limit: int = 10, offset: int = 0, type: str = "track", markets: Optional[List[str]] = None, total: Optional[int] = None) -> Dict[str, Any]:
    """
    (experimental) Searches multiple markets for an item.

    Args:
        token: Spotify user token
        query: The search query
        limit: The number of items to return (min = 1, default = 10, max = 50). If a search is to be done on multiple markets, then this limit is applied to each market
        offset: The index of the first item to return
        type: The types of items to return. One or more of 'artist', 'album', 'track', 'playlist', 'show', or 'episode'. If multiple types are desired, pass in a comma separated string
        markets: A list of ISO 3166-1 alpha-2 country codes. Search all country markets by default
        total: The total number of results to return across multiple markets and types

    Returns:
        Dictionary containing search results across multiple markets
    """
    try:
        spotify = get_spotify_client(token)
        results = spotify.search_markets(q=query, limit=limit, offset=offset, type=type, markets=markets, total=total)
        return results

    except Exception as e:
        return {"error": f"Multi-market search failed: {str(e)}"}

@mcp.tool()
def get_user_playlist(token: str, user_id: str, playlist_id: str, fields: Optional[str] = None, market: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets a specific user playlist.

    Args:
        token: Spotify user token
        user_id: The user ID
        playlist_id: The playlist ID
        fields: Which fields to return
        market: An ISO 3166-1 alpha-2 country code

    Returns:
        Dictionary containing user playlist information
    """
    try:
        spotify = get_spotify_client(token)
        result = spotify.user_playlist(user_id, playlist_id, fields=fields, market=market)
        return result

    except Exception as e:
        return {"error": f"Failed to get user playlist: {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)