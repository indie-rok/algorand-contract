## Algorand exercise

Build with:

```
algokit project run build
```

Deploy with:

```
algokit project deploy
```

## Working screenshots:

![one](./images/one.png)

![two](./images/two.png)


## Points of learning

1. Command to deploy the project is wrong (sent a PR [here](https://github.com/algorandfoundation/docs/pull/1278) to correct it)
2. While running localnet, I got an error while trying to create a wallet and send money. [this](https://github.com/algorandfoundation/algokit-cli/issues/579) helped to fix the error.
3. While creating a Box on the smart contract, we need to populate sources while sending the transaction to call the method. (its not indicated in the docs). [Discord](https://discord.com/channels/491256308461207573/1271207863766880317/threads/1301578731407540328) helped me fix it.

## Bonus: Deployed on Test network

App deployed (check box state)
[lora](https://lora.algokit.io/testnet/application/728704886)

Transaction ID:
[lora](https://lora.algokit.io/testnet/transaction/SFGHL5PS6UP64AMUUG4YISNHGF2BLBLJOHHA7SN4OYEDTUH2NPPQ)
