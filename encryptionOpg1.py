from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from time import sleep

# Generating a few keys...
print("Generating keys" )
bobKey = RSA.generate(1024)
bobSecretKey = bobKey.export_key()
bobPublicKey = bobKey.publickey().export_key()

aliceKey = RSA.generate(1024)
aliceSecretKey = aliceKey.export_key()
alicePublicKey = aliceKey.publickey().export_key()




# Herunder is functions for printing pretty
def underlineText(text):
    print(f"\n\33[4m{text}\33[0m")

def newLine(text):
    print(f"\n{text}")

def newLineBold(text):
    print(f"\n\033[1m{text}\033[0m")

# Start menu
def startMailCurrier2000():
    # Hvem skal have mail?
    underlineText("Mail currier 2000")
    newLineBold("Choose Recipient")
    print("1: Bob")
    print("2: Alice")
    recipient = input()

    if recipient == "1":
        mailCurrier(bobPublicKey,"alice")
    elif recipient == "2":
        mailCurrier(alicePublicKey,"bob")
    else:
        # Error control
        newLineBold("Error: write 1 or 2")
        sleep(1.5)
        startMailCurrier2000()

def mailCurrier(recipientPubKey,sender):
    # Mail sender
    newLineBold("Write your message")
    msg = input()
    cipherForRecipient = PKCS1_OAEP.new(RSA.import_key(recipientPubKey))
    encryptedMessage = cipherForRecipient.encrypt(msg.encode())
    print("Encrypted msg: ",encryptedMessage)
    switchAccountAndDecrypt(sender,encryptedMessage)

def switchAccountAndDecrypt(sender,encryptedMessage):
    # Wanna see the mail? Switch account! ish..
    newLineBold("Decrypt as recipient?")
    print("1 : Yes")
    print("2 : No")
    choiceDecrypt = input()
    if choiceDecrypt == "1":
        if sender == "bob":
            youGotMail(encryptedMessage,aliceSecretKey)
        if sender == "alice":
            youGotMail(encryptedMessage,bobSecretKey)
    if choiceDecrypt == "2":
        startMailCurrier2000()
        pass
    else:
        newLineBold("Enter 1 or 2 only")
        sleep(2)
        switchAccountAndDecrypt(sender,encryptedMessage)
        pass
def youGotMail(encrypedMessage,recipientSecKey):
    # Decryption and print msg
    decryptForRecipient = PKCS1_OAEP.new(RSA.import_key(recipientSecKey))
    decryptedMessage = decryptForRecipient.decrypt(encrypedMessage)
    newLineBold(decryptedMessage)
    # Restart functioning thingy - very lackluster lol
    print("Press enter to restart")
    input()
    startMailCurrier2000()

startMailCurrier2000()

