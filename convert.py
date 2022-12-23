from moviepy.editor import *
import time
import os.path
from numpy import arange
from utils import attrdict 
import random, string
import Modificators


default_settings = attrdict( 
    output_dir = 'D:\\clips\\output',
    audio_dir = 'D:\\clips\\roma-pidr.mp3',
    dir_files = 'D:\\clips\\',
    main_file = 'D:\\clips\\main\\c.mp4',
    

);

video_parts = [ 
    [	
    	attrdict(
    		formats = ('.wav', '.avi', '.wmv', '.flv', '.mpg', '.mpeg', '.mov', '.mp4'),
            end_format = '.mp4',
            volume = 0.6,
            volume2 = 0.1,
            volume_audio = 1.0,
            m_width = 1080,
            m_height = 1920,
            s_width = 400,
            s_height = 500,
            length = 3,
            position = ['center', 'center'],
            
        ),
    ]
]

def default(video_parts):
	result = []
	for i in video_parts:
		for a in i:
			result.append(mix(a))	 			

def mix(option,settings=default_settings):
	mix_array = []
	m_clip = (
		
			VideoFileClip(os.path.join(settings.main_file),
			 has_mask=True)
			.subclip(0,0 + option.length)
			.resize((option.m_width, option.m_height))
			.set_opacity(.35)
			.set_position(('left','center'))
			.fx(afx.volumex, option.volume)
			)

	audioclip = AudioFileClip(settings.audio_dir)
	audioclip_final = CompositeAudioClip([audioclip]).fx(afx.volumex,option.volume_audio)
	
	for clips in (os.listdir(settings.dir_files)):	
		if clips.endswith(option.formats):
			VideoFileClip(os.path.join(settings.dir_files,clips));			
			mix_array.append(VideoFileClip(os.path.join(settings.dir_files,clips)))
			
	for every_clip in mix_array:
		every_clip = every_clip.resize((option.m_width,option.m_height)).fx(afx.volumex,option.volume2)
		mixed = CompositeVideoClip([every_clip,m_clip.set_audio(audioclip_final)])
		mixed = mixed.subclip(0, 0 + option.length).resize((option.m_width,option.m_height))
		mixed.write_videofile(os.path.join(settings.output_dir,''.join(random.choice(string.ascii_lowercase) for i in range(5)) + f'{option.end_format}'),
							  	fps=30, 
							  	codec='libx264',
							  	)
def main():
	default(video_parts)

if __name__ == '__main__':
	main()
