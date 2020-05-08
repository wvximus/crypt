import pyAesCrypt
import os
import getpass

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

no_choice_flag = True

while no_choice_flag:

	choice = input("_N_crypt or _D_crypt: ").lower()

	# valid input, prompt filename and password
	if choice == 'n' or choice == 'd':

		no_choice_flag = False

		filename = input("Filename: ")
		password = getpass.getpass(prompt="Password: ")

		# change filename to target
		os.system(f'mv {filename} target')

		# encryption selected
		if choice == 'n':
			# encrypt
			pyAesCrypt.encryptFile('target', filename, password, bufferSize)
			# remove original file
			os.system('rm target')
		# decryption selected
		elif choice == 'd':
			# decrypt
			pyAesCrypt.decryptFile('target', filename, password, bufferSize)
			os.system('rm target')