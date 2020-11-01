# This is just a basic sequence of steps to do to undo the hashes
# TODO: Nuke this when implementing in qrm

import binascii

hexhash = "b9138e4c548d5c6579243d624d751432"

binhash = binascii.unhexlify(hexhash)

print(binhash)
