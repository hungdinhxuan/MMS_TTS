import os
import subprocess
import locale
locale.getpreferredencoding = lambda: "UTF-8"

def download(lang, tgt_extract_dir="./models", tgt_dir="./"):
  lang_fn, lang_dir = os.path.join(tgt_dir, lang+'.tar.gz'), os.path.join(tgt_extract_dir, lang)
  if not os.path.exists(tgt_extract_dir):
    os.makedirs(tgt_extract_dir)
  if os.path.exists(lang_fn):
    print(f"Model for language {lang} exists in {lang_fn}")
    if os.path.exists(lang_dir):
      print(f"Model for language {lang} exists in {lang_dir}")
      print(f"Model checkpoints in {lang_dir}: {os.listdir(lang_dir)}")
      return lang_dir
    else:
        print(f"Extracting model for language {lang} from {lang_fn} to {tgt_extract_dir}")
        
        cmd = f"tar zxvf {lang_fn} -C {tgt_extract_dir}"
        subprocess.check_output(cmd, shell=True)
        print(f"Model checkpoints in {lang_dir}: {os.listdir(lang_dir)}")
        return lang_dir
  cmd = ";".join([
        f"wget https://dl.fbaipublicfiles.com/mms/tts/{lang}.tar.gz -O {lang_fn}",
        f"tar zxvf {lang_fn} -C {tgt_extract_dir}"
  ])
  print(f"Download model for language: {lang}")
  subprocess.check_output(cmd, shell=True)
  print(f"Model checkpoints in {lang_dir}: {os.listdir(lang_dir)}")
  return lang_dir
#	English (eng), Korean (kor), Russian (rus), Vietnamese (vie), Thai (nod), Hindi (hin), Arabic (ara), French (fra), German standard (deu)
LANGS = ["eng", "kor", "rus", "vie", "nod", "hin", "ara", "fra", "deu"]

for LANG in LANGS:
    ckpt_dir = download(LANG)