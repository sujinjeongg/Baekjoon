def main():
    N = int(input())
    cards = set(map(int, input().split()))

    M = int(input())
    check_cards = list(map(int, input().split()))

    results = []
    for card in check_cards:
        if card in cards:
            results.append('1')
        else:
            results.append('0')

    print(' '.join(results))

if __name__ == "__main__":
  main()