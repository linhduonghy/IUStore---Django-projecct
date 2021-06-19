from .models import Bank, VietcomBank, VietinBank, TPBank

class BankFactory(object):

    @staticmethod
    def getBank(bankName: str) -> Bank:
        banks = {
            'VietcomBank': VietcomBank().getBank(),
            'TPBank': TPBank().getBank(),
            'VietinBank': VietinBank().getBank()
        }
        return banks.get(bankName)
