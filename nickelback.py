songs = {
  ('Nickelback', 'How You Remind Me'),
  ('Sandra McCracken', 'Oh Gracious Light'),
  ('Will.i.am', 'That Power'),
  ('Nickelback', 'Animals'),
  ('Green Day', 'Dookie'),
  ('Nickelback', 'Photograph')
}


# Create a new set that contains all songs not performed by Nickelback using conditional in comprehension

songs_by_not_nickelback = {
  a
  for a in songs 
  if a[0] != 'Nickelback'
  }

print(songs_by_not_nickelback)

# for song in songs_by_not_nickelback:
  # print(song)