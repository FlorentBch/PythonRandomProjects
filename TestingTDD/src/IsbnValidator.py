class IsbnValidator:

    def verifier_isbn(self,isbn):
        total = 0

        for i in range (10):
            total += (isbn % 10)*(i+1)
            isbn //=10
            print("total:", total)

        if total % 11 == 0:
            return True
        else:
            return False

    