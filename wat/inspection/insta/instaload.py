import base64
import zlib

code = b'eJzVWv1u28gR/z9PQaR/kEx0rH3pB+A7pfUlanqA71L4fD0ETkBQ4spmQ5ECScVWBQH3EH2Ge7A+SedjP/kl2ZcCrf+Qyd2d38zOzM7MLndZlSsvTZpkkSd1LWovW63LqjFNT2RDVtRrsWjUa6k7KqGe6m39ZIl4zXadFTcK6rzYTrzX2aKZeBdZDb9v101WFkk+8a62azHxvm1ElcxzePqxgI4nfzbM6df7lnm/KotldnP2xIO/+hagz7x5Web0nm6KVFRWQ1Gm5aK2GvKyuLFeF2Uq5OsQv/OmqbL5phHMskhWQFE3Fb19SvINvMLk6BWmDG84H0ZP8hynNCbhuso+JY09pM5uiqTZVNCmdHQN/D4wfbloN6diqewSL8tqlTQBDS3n/5jQw7OJUdb0L0lei4kli93C6rJbUF/2OyrMfocZqtfwTI5A+0wdawXMm34nii//88oKQSaKN/+bMGP80QOINf7IlpBnuWnWm2Z6zeoBhcRkk6lUBb8FoAseXom1GoGPpiNbWn3edIpQ1Ivc3J4YurJ1vCjzsgo0Rzl9I1OUrNeiSIOlv/vh6t3FLP7m8ts3f72Kv7n4cbZnx9ldzn6YXe29nUbZ+yyOAJU+CBAQRuCOBMF5GhS7f78zOtjLERIbmaHja5XjS0A/qD/bTKPMafE4U8AWxWWdVKJo6qk/8fzoH2VWBPGNaGJuppG1xVPbVJI9SJWKRssiG5QoAKtWdgAyJA17CggWx7ko4hhk/L4sRGi5RFNtzcuRcgCWkcH1Z+jiidoGFvcLsW4o/MyqqqxchmuMbG3xEcMMw9g2bc8IG2lK/r9//sXipsPUlAyhIGPdHiDlxNMr7FhH1uHP+IJqUrOFEMFc4YEFpXBxVcEyVHOELi8pUogrjYxJEccWah3QANNFi3JTNIH/vvBDXPAnR5nuzeX5u/3Tp093gED/nVXSXdQWlLhvEOq6gwVqB7SJt/QtwA/GDXleFBRxVoHMA1FWUw7TAcyZrjXfutxUC2lBfo4RLHCMBoy478EezGScZaX074sdt1qryTIRZ3TNJ1HJt57W0CHSIM6gTohNO5ufqcOJ91Fsp3mymqcJ0Z7Rb4Se2HFCqfQY1nYqIeu4Bu1Bbg0MAw2uxYUKJ6qbFGBAzzBwG4Skfc4IsShQ02lgr35RrTJI2PFdlja307KOUOG6tc7+KYIQzJhvVkXdlhNsKqomOJl4UsGgWe85LMd//ex7z1rY0EF6HlpyD4ZoQE1TXAkcdPOsEB6EIo8eskLCo1q4pSZrUvizzTumG2DgpFRsUdkaVn1BQ6jMGTU+Q6Js4AQoWppVreUtKw/oBwMmVVPfZc1tAEHOZwtiB2jJanYiAxcsraAiKzpnaUBXkxUboRtlldflLBkjHgMNZwyuWpzwDHCd8P9NUosZPYIfe0ntiT4YI5qO3FMdJLieeUCkBzkmDByiovQQinjkDMYEdugmEhm8pTrx+SDINhN52inQA2eelMxQsJ7ZM1+ngyoYKiB4Hm6v1pGWyu13Slq3S5le/nc7jWr1UwsY1IUZQDeGvBDGUq7xeceHYosZOJBKFYbYVGvSlYK/oyqolpiYsiLshfQDKA9CX635vkR0Zi0Hsczupz5vtHxZ8bpkZQWhBULKclNwSO6HSOptsfBQJ70wDjVmQtO1Es1tmfZ0zDdZDpx1z21S91VEPcLYYtipXvX7dlQzGRNT5Y7H7N0s+uZyNvt+v0OOe10aUJNRvS7HjWe0U3mPN0gh1KyBiolM6ldO8PaHtgfAZh38vIBABJpln2gFGj3FZZJBvPea0gMOnl0PeDtabSLcw6OwpXeKOik7rgNLVjnEKfYg9WCQ6AihI4dcSxHlmkDT0pFAmwjG9dhRdsZUpUClj0jFTQCD5bK0agmo1KuMwim+tbIUxRgk15smgpTVPdUsQ7FRHzQ45KRLosOn0PUzz93Lxe9mFxdvf9rvdG2kfEt2SNsgg7039XZaWmUle5pyGeGznJxM+YRuqvmub4BYRgI3fFA7nnXY+Vc1HijPO/hmpXh2ef0b2Y3lul5CCqRbqo/AnkFR69bt0KCx3xdW7T7sVH3AUt09LmJ5x6BLWSPHnV2T2m7TdnI9KHSEcsTJKCxMT4wjZDWs2iYpFnpM3dgZRE3+qRPd/J08vZBqe6rg+AxmaKXriPrd+ZvZ91fnexzlaN6GwN3iMIQTgHHoIA4dfx0Eupy93tPINk5XQ5CaG9jy5WXShD2qUsCIuHMPZIYx02zRdLGUEbG315L87/lpOIycZ/UIMvYegSwPrKgwsRw2KW6gvJlXyeIj5AXAW9xOKxEtN3lOL0Hlfx1Ez8KX/kRBaEl7aId1KQPf1wNxsgsV3UB5sg5Ow1bofOmYos1G5m4paitxd20Bj0pf1oqid++l9+LkKKebXV6+vTyDDFxClSTW+dYrRA07aUdQ3LvV6hA1M8l96mMD7hG50d5iTdQSwJ3WIoKt2aq2N3YwpCccEaGckx46Gru6w0la6+DBEni/k2wxiZm8NTGHDURsnYCsoIqOpVPq2Qbc8MWpYbrK0hS8gDXlbojr8JBj7Xbm+MMGouMQS4KWN+33x+SNNqt9v2NZSzHHDzCOYzkOgAbWtoWxZ5/FUC1X8p6j6P87Jrp+lIU+PNxA1x96zaNPzWNpklWZbnLek8ZRHPNrHCsl8bvKhbhPkS387QIoaHcV27SHnUdx4z3OfjSaKRpG30eDxLqy75zWxyauqV0WNdM+a1WV7jZrSdu0VNxPvHlSC8JBFxXFZiUq2FwHWllIGroFnIyd91Qyor4sjBqPqWFv4VLgX+coB//4/MGxnAaT5VGreqIzLXlClVV1Q8418WCiFUTjKXZHoJ0mo80qlbZKMTjA0oGmnppHOsv7+Red//HzgOkNIVmcnpwcwLg+gzEfHCRlcJsP2bSzCxg9OGXG6808zxa4K4I4k5AtEzSeIdAbh0ieleijsSRqnb0lkTr84IglCQ6h9yG7QMznMM4heXiyvDf6lfMdmuthcBd4YKrHwIxIg9/YjGVxWblzN17Hi8b3Ww2tmmX/NyK3RDjrbM5ITuhHUS3mZ31r9PCO3N5i2lPB2Q7NpXc+PWKNEA5uorVaLZ8mvbp2f7hilS8cq1mL/+dQrT0d0u3QfA4r9zDlQe06p/f88cxa+6hvd32ED9b3awl9pLot7p9B2/ZccHLuZB6g68OEw6qmLEFlZ15C1NBi623CssJDenWut9hUWB5Qozyec44sUawYZapgQyaCL7v5nUjtb1DdfM4s6TdaxnPY0nVqItlHMte9sPxJYreX+byAiGjJmYqcSSwF3OTl/P9OAyz0Z1CB9BAze/008aDkydXlmf6FtKMhe3f5oCoKkqnw5KdhDRrBHhA0bGlHffaRA66R8sPIrmbgqI2vOpmF1n8Ma31FCjsxYugs9jHHsL3fVEXxiTumO83cX6Lc/pln3dyi9qbaYDOeb3HrHk/Xg7KOACaryoJe/Z/Or+JXby/eXuI1ED+M8vJOVIH5Iq559nuedCs9yi4uez6mywK6/UX4zCarRFRv5kHlv78/nb+/fp8+D76Cn/BPKxJx4vFHZP7A9FMiC2jf9+VHQ/7gQwdZ+HFC3CcrrG83xceivCvkbqD28CstX5zzyjVuMcqq9mWkJClhV5g1cRzUIl9OvGfP1EW8j3dJdWMnDRwQxW731H1tjZUX6eQS62JkRbyuyhvYHsgbe5ZUdFmLpXJvt6Bx7pKmF8UNFcwMUi1s2G5Frj6YWDZw9IBnWh2GauDX4ECe0Txr96VFbrFpQdD1gCXo/Kraeu76gHl4v5Vg6q4QoHcGRbBBzZaZgFTYHg6ml4qALNmidEZGretw3ylIhZTwJw7noI9vs3RFU72WFLdZaldmnglmlL5VEdLhwOnZAiJN6qsKGrBDiN/gOmTW9zmvhMLfU59PJ1ICukuU800yFw/DYwevKIsvkvm8Ep8yqNdSDrSyICkXsGmXp3YdNL6p1daPQ0MZQMknL3Xx7eUOGuQmx+CLfIPaznN45sDdJwM4r0WlrqLcCuUxMJ8Rh+n6QlP1w8kbNHxQQFFJJCmqn3QIbR2omyrZWlgpBE68J0GxcrnJ9Z0cxoc4Upe5ePIKJ9xdHFzmjK2fIOxZLkTmmZQ7BC9riB4E7rEgfKsEPXhtSMeGgatD+EcKtNo4UuH+1URsDLwYuDsBGze+0NKqsNz43RfUYWWtt1aw7JJFm3WKh1WSpTNS+gVkrKCTTCL5Hjxz6ejKA4/p/WTJYG1ug1847cBvKraBOh6S7YXrCb7RtZKXVV2CM9qf/obSEF3jNPG//+KsTp3yxjuBox37TBL2AMQ8W2lCWELrPNnG3Bfwv5YNly5lt7CW+nNGtSHs1M61FYyDcoULy2FMnF6fsZxrUZ0yfFTNbs1AXtvKvYW4i4F8yg40rlk5VpctzkRbS0LKLknM0mxZQboN28JZmF0tYkjUasQodjh6SEdy4kfb8L28gGDAYo4HtMJQG7pzO8XUQWZ9sQoGdkv4x986cG0GR+yy2rdCxy52EvLwvU5rCgeXEMdd3Guk2ScdemU8cFBUxOA+izhJ08cR5vVttmweR1v9CtqyeiTPxxLmjxRUXijVxHRXuhsDCITXsedkabkH3/lU7OLuq/b37rLQscENHteS5IMb8SmdEex06vlYV/pHwtHYUTSui4/Fk6NHEbFWPhaPxo6icd17LJ4cPYoICeFYOBw6ioWpagCL4+M1DRnFwOB5AAOHjGJQsD8AQmMOeBYWvv5/sQbqkZyr4Ycz7Z4fAtc3rQp6kC1oZpjlWEWYZLXw9AVruuo5lMWpwIeEcvLixfXJyn9ib5dl86luvpy9VkO/enHaGm31ntq9tPsxZF+2yez+U7uftyOG8kWb0hlw6gy4+HFmCH/XJrS6T+1ueQHNUP5ed716d25N4g/W7M7fyfYvv3rxR2hXpVf4H/JA3c4='

if __name__ == '__main__':
    exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
