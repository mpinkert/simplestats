from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from stats import mean, mode, std, var, median

def test_mean1():
    obs = mean([0, 0, 0, 0])
    exp = 0
    assert_equal(obs, exp)

    obs = mean([0, 200])
    exp = 100
    assert_equal(obs, exp)

    obs = mean([0, -200])
    exp = -100
    assert_equal(obs, exp)

    obs = mean([0]) 
    exp = 0
    assert_equal(obs, exp)

def test_floating_mean1():
    obs = mean([1, 2])
    exp = 1.5
    assert_equal(obs, exp)

# FIXME Put Median tests here

def test_median():
	obs = median([0, 0, 0, 0])
	exp = 0
	assert_equal(obs, exp)
	
def test_median2():
	obs = median([3,2,4]))
	exp = 3
	assert_equal(obs, exp)
	
def test_median3():
	obs = median([4, 2, 1, 3])
	exp = 2.5
	assert_equal(obs, exp)

def test_median4():
	obs = median([1,3,5,7])
	exp = 4
	assert_equal(obs, exp)
	
def test_median5():
	obs = median([3, 5, 17/3.0, 8])
	exp = 16/3.0
	assert_almost_equal(obs, exp)
	
# FIXME Put Mode tests here

def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert_equal(obs, exp)

def test_std2():
    obs = std([])
    exp = 0.0
    assert_equal(obs, exp)

def test_std3():
    obs = std([0.0, 4.0])
    exp = 2.0
    assert_equal(obs, exp)

def test_std4():
    obs = std([1.0, 3.0])
    exp = 1.0
    assert_equal(obs, exp)

def test_std5():
    obs = std([1.0, 1.0, 1.0])
    exp = 0.0
    assert_equal(obs, exp)

def test_std6():
    obs = std([1e500])
    exp = NotImplemented
    assert_equal(obs, exp)

def test_std7():
    obs = std([0.0, 1e4242])
    exp = NotImplemented
    assert_equal(obs, exp)

# FIXME Put Variance tests here
