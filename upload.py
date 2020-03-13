import os
from git import Repo
import sys
import argparse
import logging
import shutil

parse = argparse.ArgumentParser()
parse.add_argument("imglist", nargs='+', help="image list")
args = parse.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)


def main():
    logger.info(__file__)
    imglist = args.imglist
    # logger.info(imglist)
    repo = Repo()
    git = repo.git
    giturl = 'https: // github.com/hfutjcd/tuchuang/blob/master/'
    result=[]
    git.add(__file__)
    # logger.info(git.status())
    for img in imglist:
        imgPath = os.path.normpath(img)
        # imgname = os.path.abspath(imgPath)
        imgname = os.path.basename(imgPath)
        foldname = os.path.basename(os.path.dirname(imgPath))
        if not foldname:
            foldname = 'commonimge'
        if not os.path.exists(foldname):
            os.mkdir(foldname)
        newpath=os.path.join(foldname,imgname)
        shutil.copy(imgPath,newpath)
        git.add(newpath)
        result.append(giturl+"{}/{}?raw=true".format(foldname,imgname))
        logger.info(imgname)
        logger.info(os.path.basename(os.path.dirname(imgPath)))
    git.commit('-m',"add img to {}".format(foldname))
    remote = repo.remote('origin') 
    remote.push()  # Authentication failed for
    # logger.info(result)
    for url in result:
        print(url)
if __name__ == "__main__":
    main()
