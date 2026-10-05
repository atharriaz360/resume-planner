"""Run after record-interactions.cjs; requires FFmpeg on PATH or FFMPEG env."""
import os,subprocess,shutil
from pathlib import Path
R=Path(__file__).resolve().parent
ff=os.environ.get('FFMPEG') or shutil.which('ffmpeg')
if not ff:raise SystemExit('Install FFmpeg, or set FFMPEG to its executable path.')
subprocess.run([ff,'-y','-f','concat','-safe','0','-i',str(R/'frames.txt'),'-vf','setpts=PTS/1.5,fps=30','-an','-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(R/'Resume-Studio-Interactive.mp4')],check=True)
