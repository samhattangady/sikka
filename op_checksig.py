import ecdsa
import hashlib
from ecdsa import VerifyingKey
from helpers import deserialize as d

Sig = '3045022100e5aed3d9c4b32bbfbd9b64a649b377aa6251061d3b379f35303c5711f847b4f5022067883832ae4af1bc7797dcf5fde00af91a87fe7db94f12cd7bb12968fbbc518701'
"""
Signature is DER encoded
From https://github.com/bitcoinbook/bitcoinbook/blob/second_edition/ch06.asciidoc

0x30—indicating the start of a DER sequence
0x45—the length of the sequence (69 bytes)
0x02—an integer value follows
0x21—the length of the integer (33 bytes)
R—e5aed3d9c4b32bbfbd9b64a649b377aa6251061d3b379f35303c5711f847b4f5
0x02—another integer follows
0x20—the length of the integer (32 bytes)
S-67883832ae4af1bc7797dcf5fde00af91a87fe7db94f12cd7bb12968fbbc5187
A suffix (0x01) indicating the type of hash used (SIGHASH_ALL)
"""
r = 'e5aed3d9c4b32bbfbd9b64a649b377aa6251061d3b379f35303c5711f847b4f5'
s = '67883832ae4af1bc7797dcf5fde00af91a87fe7db94f12cd7bb12968fbbc5187'

pubkey = '0407aaeac6db35f79e810a0b187255c461d2c075b999edd17684ca342f985974930bcae1c3e20c1a07ca3d58a51b7227fa0a84774651a0fdbf346d3f2b8b765d6b'
ripemd160 = hashlib.new('ripemd160')
pubkey_hash160 =  ripemd160.update(bytes.fromhex(pubkey[2:]))
pubkey_hash160 = ripemd160.hexdigest()

# pk_script
# 1976a914bc341fdc8f995bcb117ce7eecdad2ee50d6f7e1f88ac

raw_tx = '010000000194ed8510f74214060402aff12a9d28aca082a9e85abb80a2d4e6fb8fa77e5268010000008b483045022100e5aed3d9c4b32bbfbd9b64a649b377aa6251061d3b379f35303c5711f847b4f5022067883832ae4af1bc7797dcf5fde00af91a87fe7db94f12cd7bb12968fbbc518701410407aaeac6db35f79e810a0b187255c461d2c075b999edd17684ca342f985974930bcae1c3e20c1a07ca3d58a51b7227fa0a84774651a0fdbf346d3f2b8b765d6b ffffffff017fd14b00000000001976a914170847eab6687ed1d2959467ed3c887a8e1ecc8088ac00000000'
# replace sig script with pk_script and add hash value to the end
new_tx = '010000000194ed8510f74214060402aff12a9d28aca082a9e85abb80a2d4e6fb8fa77e5268010000001976a914bc341fdc8f995bcb117ce7eecdad2ee50d6f7e1f88acffffffff017fd14b00000000001976a914170847eab6687ed1d2959467ed3c887a8e1ecc8088ac0000000001000000'

hashed_message = hashlib.sha256(bytes.fromhex(new_tx)).hexdigest()
vk = VerifyingKey.from_string(bytes.fromhex(pubkey[2:]), curve=ecdsa.SECP256k1)
vk.verify(bytes.fromhex(r+s), bytes.fromhex(hashed_message), hashlib.sha256)

print('verified')