path = "."

# Set this to True to fully unlock all maps
# Set this to False to erase all map progress
# Set to None to convert map progress
useFullMaps = None

def reverse_endianness_block2(block):
  even = block[::2]
  odd = block[1::2]
  res = []
  for e, o in zip(even, odd):
    res += [o, e]
  return res

# Initiate base file
data = None
saveFile = [0]*257678
saveFile[:4] = [0x42, 0x4c, 0x48, 0x54]
saveFile[0x67] = 0x01

# Copy over character unlock flags
with open(path+"/PCF01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x5:0x3d] = data[0x1:0x39] # Extract only relevant part

# Copy over achievement status flags
with open(path+"/PAM01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x68:0x0d0] = data[0x00:0x68] # Extract regular disk part
saveFile[0xd6:0x10a] = data[0x6e:0xa2] # Extract plus disk part

# Copy over achievement notification status flags
with open(path+"/PAC01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x130:0x198] = data[0x00:0x68] # Extract regular disk part
saveFile[0x19e:0x1d2] = data[0x6e:0xa2] # Extract plus disk part

# Copy over bestiary information
with open(path+"/PKO01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x2c2:0x4c22] = data[0xca:0x4a2a]
saveFile[0x2c2:0x4c22] = reverse_endianness_block2(saveFile[0x2c2:0x4c22])

# Copy over party formation
with open(path+"/PPC01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x5018:0x5024] = data[:] # All bytes are relevant

# Copy over misc information from game
with open(path+"/PEX01.ngd", 'rb') as f:
  data = f.read()
offset = 0x540c
saveFile[offset+0x00:offset+0x08] = data[0x00:0x08][::-1] # Cumulative EXP
saveFile[offset+0x08:offset+0x10] = data[0x08:0x10][::-1] # Cumulative Money
saveFile[offset+0x10:offset+0x18] = data[0x10:0x18][::-1] # Current money
saveFile[offset+0x18:offset+0x20] = data[0x18:0x20][::-1] # Number of battles
saveFile[offset+0x20:offset+0x24] = data[0x20:0x24][::-1] # Number of game overs
saveFile[offset+0x24:offset+0x28] = data[0x24:0x28][::-1] # Play time in seconds
saveFile[offset+0x28:offset+0x2c] = data[0x28:0x2c][::-1] # Number of treasures
saveFile[offset+0x2c:offset+0x30] = data[0x2c:0x30][::-1] # Number of crafts
saveFile[offset+0x30:offset+0x34] = data[0x30:0x34][::-1] # Unused data
saveFile[offset+0x34] = data[0x34] # Highest floor
saveFile[offset+0x35:offset+0x39] = data[0x35:0x39][::-1] # Number of locked treasures
saveFile[offset+0x39:offset+0x3d] = data[0x39:0x3d][::-1] # Number of escaped battles
saveFile[offset+0x3d:offset+0x41] = data[0x3d:0x41][::-1] # Number of dungeon enters
saveFile[offset+0x41:offset+0x45] = data[0x41:0x45][::-1] # Number of item drops
saveFile[offset+0x45:offset+0x49] = data[0x45:0x49][::-1] # Number of FOEs killed
saveFile[offset+0x49:offset+0x51] = data[0x49:0x51][::-1] # Number of steps taken
saveFile[offset+0x51:offset+0x59] = data[0x51:0x59][::-1] # Money spent on shop
saveFile[offset+0x59:offset+0x61] = data[0x59:0x61][::-1] # Money sold on shop
saveFile[offset+0x61:offset+0x69] = data[0x61:0x69][::-1] # Most EXP from 1 dive
saveFile[offset+0x69:offset+0x71] = data[0x69:0x71][::-1] # Most Money from 1 dive
saveFile[offset+0x71:offset+0x75] = data[0x71:0x75][::-1] # Most Drops from 1 dive
saveFile[offset+0x75] = data[0x75] # Unknown data
saveFile[offset+0x76:offset+0x7e] = data[0x76:0x7e][::-1] # Number of library enhances
saveFile[offset+0x7e:offset+0x82] = data[0x7e:0x82][::-1] # Highest battle streak
saveFile[offset+0x82:offset+0x86] = data[0x82:0x86][::-1] # Highest escape streak
saveFile[offset+0x86] = data[0x86] # Hard mode flag
saveFile[offset+0x87] = data[0x87] # IC enabled flag
# saveFile[offset+0x88:offset+0xae] = data[0x88:0xae] # Unknown data
saveFile[offset+0xae:offset+0xb2] = data[0xae:0xb2][::-1] # IC floor
saveFile[offset+0xb2:offset+0xb6] = data[0xb2:0xb6][::-1] # Number of akyuu trades
saveFile[offset+0xb6:offset+0xba] = data[0xb6:0xba][::-1] # Unknown data

# Copy over event flags
with open(path+"/EVF01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x54c6:0x68b2] = data[0x0:0x13ec] # Extract only relevant part

# Copy over item discovery flags
with open(path+"/EEF01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x7bd7:0x7c13] = data[0x001:0x03d] # Extract main equips
saveFile[0x7c9f:0x7d8f] = data[0x0c9:0x1b9] # Extract sub equips
saveFile[0x7dcb:0x7e2f] = data[0x1f5:0x259] # Extract materials
saveFile[0x7ef7:0x7fab] = data[0x321:0x3d5] # Extract special items

# Copy over item inventory count
with open(path+"/EEN01.ngd", 'rb') as f:
  data = f.read()
saveFile[0x83a8:0x8420] = data[0x002:0x07a] # Extract main equips
saveFile[0x8538:0x8718] = data[0x192:0x372] # Extract sub equips
saveFile[0x8790:0x8858] = data[0x3ea:0x4b2] # Extract materials
saveFile[0x89e8:0x8b50] = data[0x642:0x7aa] # Extract special items
saveFile[0x83a8:0x8420] = reverse_endianness_block2(saveFile[0x83a8:0x8420])
saveFile[0x8538:0x8718] = reverse_endianness_block2(saveFile[0x8538:0x8718])
saveFile[0x8790:0x8858] = reverse_endianness_block2(saveFile[0x8790:0x8858])
saveFile[0x89e8:0x8b50] = reverse_endianness_block2(saveFile[0x89e8:0x8b50])

# Copy over character data
offset = 0x9346
for i in range(1, 57):
  str_i = "0"+str(i) if i < 10 else str(i)
  with open(path+"/C"+str_i+".ngd", 'rb') as f:
    data = f.read()
  saveFile[offset+0x000:offset+0x004] = data[0x000:0x004][::-1] # Level
  saveFile[offset+0x004:offset+0x00c] = data[0x004:0x00c][::-1] # EXP
  for s in range(14): # HP -> SPD, then FIR -> PHY
    start = 0xc + (s*4)
    end = start + 4
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Library level
  for s in range(6): # HP -> SPD
    start = 0x44 + (s*4)
    end = start + 4
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Level up bonus
  saveFile[offset+0x05c:offset+0x060] = data[0x05c:0x060][::-1] # Subclass
  for s in range(40): # 12 boost, 6 empty, 2 exp, 10 personal, 10 spells
    start = 0x60 + (s*2)
    end = start + 2
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Skill level
  for s in range(20): # 10 passives, 10 spells
    start = 0xb0 + (s*2)
    end = start + 2
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Subclass skill level
  for s in range(12): # HP, MP, TP, ATK -> SPD, ACC, EVA, AFF, RES
    start = 0xd8 + (s*1)
    end = start + 1
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Tome flags
  for s in range(8): # HP, MP, TP, ATK -> SPD
    start = 0xe4 + (s*1)
    end = start + 1
    saveFile[offset+start:offset+end] = data[start:end][::-1] # Boost flags
  saveFile[offset+0x0ec:offset+0x0ee] = data[0x0ed:0x0ef][::-1] # Unused skill points
  saveFile[offset+0x0ee:offset+0x0f2] = data[0x0f0:0x0f4][::-1] # Unused level up bonus
  for s in range(8): # HP, MP, TP, ATK -> SPD
    start = 0xf2 + (s*2)
    end = start + 2
    saveFile[offset+start:offset+end] = data[start+2:end+2][::-1] # Gem count
  saveFile[offset+0x102] = data[0x104] # Used training manuals
  saveFile[offset+0x103:offset+0x107] = data[0x105:0x109][::-1] # BP count
  for s in range(4): # main, 3 sub equips
    start = 0x107 + (s*2)
    end = start + 2
    saveFile[offset+start:offset+end] = data[start+2:end+2][::-1] # Equip ID
  offset += 0x10f

# Fully unlock maps
if (useFullMaps):
  saveFile[0x0ce8e:0x2ae8e] = [0x55]*0x1e000 # 30 floors
  saveFile[0x33e8e:0x3ee8e] = [0x55]*0xb000  # 11 underground floors
  #(B1F is D40.txt; 31-39 are unused)
elif (useFullMaps is None):
  #Old map format: 1 byte per cell. Squares are either "#" (explored) or "." (unexplored)
  #New map format: 2 bits per cell, packed together for 4 squares per byte.
  #Data is "rotated", meaning the first "line" in the new format is the first column of the old data.
  #0x00 is fully unexplored, 0x55 (i.e. 0101 0101) is fully explored.
  #The maps are the same size as in the standalone version. All maps are 128x128.
  hashmap = {'.' : 0, '#' : 1}
  mapstart = 0x0ce8e
  newMapsize = 128*128//4
  for i in range(50):
    filename = f'D{i+1:02}.txt'
    with open(path+"/"+filename, 'r') as f:
      data = f.readlines()
      assert(len(data) == 128)
    #Read in 4 bytes at once from each file. Need to go "sideways" and read columns first, then rows.
    #Pack the result into a single byte, ORing and offsetting each bit
    for x in range(newMapsize):
      byteval = (hashmap[data[(x*4+0) % 128][(x*4+0) // 128]] << 0 |
                 hashmap[data[(x*4+1) % 128][(x*4+1) // 128]] << 2 |
                 hashmap[data[(x*4+2) % 128][(x*4+2) // 128]] << 4 |
                 hashmap[data[(x*4+3) % 128][(x*4+3) // 128]] << 6)
      saveFile[mapstart+x] = byteval
    mapstart += newMapsize
  assert(mapstart == 0x3ee8e)
#

# A decrypted file for debugging
with open(path+"/result-decrypted.dat", 'wb') as f:
  f.write(bytes(saveFile))
saveFile = [((i & 0xff) ^ c) for i, c in enumerate(saveFile)]
# The final file
with open(path+"/result.dat", 'wb') as f:
  f.write(bytes(saveFile))
