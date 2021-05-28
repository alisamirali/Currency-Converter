from tkinter import *


class CurrencyConverter:
    def __init__(self):
        window = Tk()  # Create application window
        window.title("Currency Converter By: Ali Samir")  # Add title to application window
        window.configure(bg="teal")  # Add background color to application window

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="teal", text="Amount to convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="teal", text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="teal", text="Converted Amount = ").grid(row=3, column=1, sticky=W)

        # Create objects and add entry functions
        self.amountToConvertVar = StringVar()
        Entry(window, textvariable=self.amountToConvertVar, justify=RIGHT).grid(row=1, column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable=self.conversionRateVar, justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        Label(window, font="Helvetica 12 bold", bg="teal",
              textvariable=self.convertedAmountVar).grid(row=3, column=2, sticky=E)

        # Create convert and clear buttons.
        Button(window, text="Convert", font="Helvetica 12 bold", bg="blue", fg="white",
               command=self.ConvertedAmount).grid(row=4, column=2, sticky=E)
        Button(window, text="Clear", font="Helvetica 12 bold", bg="red", fg="white",
               command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()  # Runs the application program

    # Function to do the conversion. Stores inputs and performs conversion
    def ConvertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amountToConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

    # Function to clear inputs
    def delete_all(self):
        self.amountToConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")


CurrencyConverter()