
1) UPDATED: Image Classification script

- CHANGED: In the image data generator part, changed the 'binary' into 'sparse'. Kasi kinopya ko lang previously yung code na yun. Eh yung pinagkopyahan ko eh either cat or dog lang ang choice (binary), eh yung categories natin eh 42 types (sparse categorical).
- ADDED: CSV Generator at the end
- ADDED: Data Augmentation training. Basta dinidistort nung keras yung image slightly (for improved and more versatile image detection)



2) ADDED: MobileNet Image Classification

- Tinry ko gamitin to before, napakabagal nung training and ram intensive. So hindi ko pinursue, pero eto yung code. Inextend ko lang yung original 'Image Class' script. In this code, ang ginamit ko is yung light 'MobileNet architecture'
- Pwede babaan yung batch_size para mas magoperate ng maayos yung program.


3) IMPORTANT!!! : Create an empty 'test' Folder

- Ilagay mo dito lahat nung images galing sa shopee. Di ko na inupload sa github dahil sobrang laki


4) ADDED: test.csv

- HEADS UP, mas marami yung images sa folder compared dun sa nakalista dito. Sabi ng shopee, kung ano lang yung nakalista dito, iyon lang yung ipepredict mo