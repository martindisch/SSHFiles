import os

def get_videos(filepath):
    """Build a list of names and absolute paths of videos in `filepath`.

    Parameters
    ----------
    filepath : str
        The directory to recursively search for video files

    Returns
    -------
    list
        List of lists with filenames and absolute paths sorted by filename
    """
    video_exts = [
        "3g2", "3gp", "aaf", "asf", "avchd", "avi", "drc", "flv", "m2v", "m4p",
        "m4v", "mkv", "mng", "mov", "mp2", "mp4", "mpe", "mpeg", "mpg", "mpv",
        "mxf", "nsv", "ogg", "ogv", "qt", "rm", "rmvb", "roq", "svi", "vob",
        "webm", "wmv", "yuv"
    ]
    videos = []
    for root, subdirs, files in os.walk(filepath):
        videos.extend(
            ([f, os.path.join(os.path.abspath(root), f)] for f in files if
            f.split('.')[-1] in video_exts)
        )
    videos.sort(key=lambda x: x[0].lower())
    return videos

def make_urls(files, username, ip):
    """Replace the absolute paths in the file list with SFTP URLs.

    This will happen in-place, meaning that the given list of lists will be
    modified directly to save memory.

    Parameters
    ----------
    files : list
        List of lists with filename and absolute path for every file
    username : str
        The username to use for the URL
    ip : str
        The address to user for the URL
    """
    # Build prefix once
    prefix = "sftp://{}@{}:".format(username, ip)
    # Go through all sublists
    for i in range(len(files)):
        # Modify the file path directly
        files[i][1] = prefix + files[i][1]
