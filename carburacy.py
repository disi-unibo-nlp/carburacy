import math
import argparse

parser = argparse.ArgumentParser('Compute Carburacy')
parser.add_argument('--alpha', default=10, type=float)
parser.add_argument('--beta_train', default=1, type=int)
parser.add_argument('--beta_test', default=100, type=int)
parser.add_argument('--score', required=True, type=float)
parser.add_argument('--emission_train', required=True, type=float)
parser.add_argument('--emission_test', required=True, type=float)

def compute_carburacy_train_test(score, emission, alpha, beta):
    carb = math.exp(math.log(score, alpha)) / (1 + emission * beta)
    return carb

def compute_carburacy_from_train_test(carb_train, carb_test):
    carb = (2 * carb_test * carb_train) / (carb_train + carb_test)
    return carb

def compute_carburacy(score, emission_train, emission_test, alpha, beta_train, beta_test):
    train = compute_carburacy_train_test(score, emission_train, alpha, beta_train)
    test = compute_carburacy_train_test(score, emission_test, alpha, beta_test)
    carb = compute_carburacy_from_train_test(train, test)
    return carb, train, test


if __name__ == '__main__':
    args = parser.parse_args()
    score = args.score
    emission_train, emission_test = args.emission_train, args.emission_test
    alpha = args.alpha
    beta_train, beta_test = args.beta_train, args.beta_test

    carb, train, test = compute_carburacy(score, emission_train, emission_test, alpha, beta_train, beta_test)
    print(f'Carburacy: {carb}')
    print(f'Train: {train}')
    print(f'Test: {test}')

