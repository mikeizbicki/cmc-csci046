import os
import glob
import zipfile


def read_from_zipfile(input_path):
    '''
    A generator containing the tweets stored in input_path.
    The file located at input_path is assumed to be a zip file,
    where every file contained within the zipfile is a newline separated list of JSON objects.
    '''
    with zipfile.ZipFile(input_path) as archive:
        for filename in sorted(archive.namelist()):
            with archive.open(filename) as f:
                for line in f:
                    yield json.loads(line)


def read_from_dir(input_path):
    '''
    A generator containing the tweets stored in input_path.
    The variable input_path is assumed to reference a directory,
    and the generator will loop through all of the zip files in the directory *in alphabetical order*.
    If there are files in the directory that are not zip files
    (i.e. they do not end in ".zip"),
    then these files will be ignored.

    YOU MUST:
    Call the read_from_zipfile function you created above for each path returned by glob.

    HINT:
    Use the yield from syntax to access the generator returned by read_from_zipfile.

    HINT:
    Use python's glob library to get the list of zip files.
    '''
    glob_path = os.path.join(input_path,'*.zip')
    paths = sorted(glob.glob(glob_path))
    for path in paths:
        yield from read_from_zipfile(path)
        #for tweet in read_from_zipfile(path)
            #yield tweet

