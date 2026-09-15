import pytest

from primes.prime_finder import PrimeFinder


@pytest.fixture
def prime_finder():
    return PrimeFinder()


class TestIsPrime:
    @pytest.mark.parametrize("n", [0, 1])
    def test_returns_false_given_zero_and_one(self, prime_finder, n):
        # given n is either 0 or 1 (non-prime numbers)

        # when checking if n is prime
        result = prime_finder.is_prime(n)

        # then the result of is_prime should be False
        assert not result


class TestFirstNPrimes:
    @pytest.mark.parametrize("length", [0, -1, -10])
    def test_raises_value_error_given_an_invalid_length(self, prime_finder, length):
        # given a non-positive length, when generating a list of primes
        # then a ValueError should be raised
        with pytest.raises(ValueError):
            _ = prime_finder.list_first_n_primes(length)

    @pytest.mark.parametrize("length", [1, 10, 1000])
    def test_has_correct_number_of_elements_given_a_valid_length(self, prime_finder, length):
        # given a valid fixed length

        # when generating a list of primes
        list_of_primes = prime_finder.list_first_n_primes(length)

        # then the total number of primes in list should equal to the given length
        assert len(list_of_primes) == length
