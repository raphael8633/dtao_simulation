class Subnet:
    def __init__(self, name: str, alpha_in: float, alpha_out: float, tao: float):
        """
        Initialize a Subnet instance with alpha_in, alpha_out, and tao.
        """
        self.name = name
        self.alpha_in = alpha_in
        self.alpha_out = alpha_out
        self.tao = tao

    def price_from_tao(self, input_tao: float) -> float:
        """
        Calculate price using the formula: (input * alpha_in) / (tao + input).
        """
        return (input_tao * self.alpha_in) / (self.tao + input_tao)

    def price_from_alpha(self, input_alpha: float) -> float:
        """
        Calculate price using the formula: (input * tao) / (alpha_in + input).
        """
        return (input_alpha * self.tao) / (self.alpha_in + input_alpha)
    
    # print subnet status
    def print_status(self):
        print(f"{self.name}:")
        print(f"alpha_in={self.alpha_in}, alpha_out={self.alpha_out}, tao={self.tao}")
        #print price from tao, input_tao = 10^8, and out put / 10^8 to avoid floating point error
        print(f"Price from tao: {self.price_from_tao(input_tao=1)}")
        #print price from alpha, input_alpha = 10^8, and out put / 10^8 to avoid floating point error
        print(f"Price from alpha: {self.price_from_alpha(input_alpha=1) }")

class Network:
    def __init__(self):
        self.subnets = []
    # simulate block
    def forwardBlock(self, block_size: int):
        # tao emit
        #TODO: 
        return
    def addSubnet(self, subnet: Subnet):
        self.subnets.append(subnet)
    def printSubnetWeight(self):
        # count subnet weight base on tao
        total_tao = 0
        for subnet in self.subnets:
            total_tao += subnet.tao
        for subnet in self.subnets:
            print(f"{subnet.name}: {subnet.tao / total_tao}")
            
class Account:
    def __init__(self, name: str, tao_balance: float):
        self.name = name
        self.tao_balance = tao_balance
        # a dictionary to store alpha holding
        self.alpha_holding = {}
    # buy alpha from subnet
    def buyAlpha(self, subnet: Subnet, tao_amount: float):
        output_alpha = subnet.price_from_tao(tao_amount)
        self.tao_balance -= tao_amount
        subnet.tao += tao_amount
        subnet.alpha_in -= output_alpha
        # check if already exist in alpha_holding
        if subnet.name in self.alpha_holding:
            self.alpha_holding[subnet.name] += output_alpha
        else:
            self.alpha_holding[subnet.name] = output_alpha
        return output_alpha
    # print account status
    def print_status(self):
        print(f"{self.name}:")
        print(f"tao_balance: {self.tao_balance}")
        print(f"alpha_holding: {self.alpha_holding}")
    
# Example usage for testing
# subnets
subnet1 = Subnet("SN1", alpha_in=1, alpha_out=1, tao=1)
subnet2 = Subnet("SN2", alpha_in=1, alpha_out=1, tao=1)
# network
network = Network()
network.addSubnet(subnet1)
network.addSubnet(subnet2)
#network.printSubnetWeight()
# account
account1 = Account("acc0", tao_balance=1000)
account1.buyAlpha(subnet1, tao_amount=100)
account1.print_status()

