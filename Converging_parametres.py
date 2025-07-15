"""
By 'converging parametres' I mean any set of parametres that doesn't cause the population or the resource to diverges. To find most of them I used a program to checks if the absolute value of the "final value" of both the resources and the population is below 100 for a range of parametres. 
I'll add them when Im satisfied with the set of parametres I get.

The 'simulation time' parametre is the time at which the system converges, it does not affect the system in any way therefore i would recommend sticking to a high value of simulation time in order to have a global view of the system's growth.
"""

# this one is an interesting one I found when messing around with the parametres.
init_pop = 5
init_res = 11
init_growth = 0.01
init_consumption = 0.2422
init_replenishment = 0.989
dt = 0.01
simulation_time = 2000


# and here is a fraction of the ones my program found (note that most of them are going to look similare to each other making them not as interesting)

# Parameter Set 1
init_pop = 1
init_res = 1
init_growth = 0.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 920

# Parameter Set 2
init_pop = 1
init_res = 1
init_growth = 0.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 792

# Parameter Set 3
init_pop = 1
init_res = 1
init_growth = 0.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 634

# Parameter Set 4
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 132

# Parameter Set 5
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 142

# Parameter Set 6
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 145

# Parameter Set 7
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 153

# Parameter Set 8
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 79

# Parameter Set 9
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 84

# Parameter Set 10
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 93

# Parameter Set 11
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 100

# Parameter Set 12
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 71

# Parameter Set 13
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 72

# Parameter Set 14
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 78

# Parameter Set 15
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 84

# Parameter Set 16
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 71

# Parameter Set 17
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 72

# Parameter Set 18
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 68

# Parameter Set 19
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 73

# Parameter Set 20
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 71

# Parameter Set 21
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 72

# Parameter Set 22
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 71

# Parameter Set 23
init_pop = 1
init_res = 1
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 24
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 56

# Parameter Set 25
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 70

# Parameter Set 26
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 76

# Parameter Set 27
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 78

# Parameter Set 28
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 82

# Parameter Set 29
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 39

# Parameter Set 30
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 46

# Parameter Set 31
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 32
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 33
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 34
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 42

# Parameter Set 35
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 36
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 37
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 47

# Parameter Set 38
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 39
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 40
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 41
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 42
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 43
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 44
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 45
init_pop = 1
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 46
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 43

# Parameter Set 47
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 48
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 55

# Parameter Set 49
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 50
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 51
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 52
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 53
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 54
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 55
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 56
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 57
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 58
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 59
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 60
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 61
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 62
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 63
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 64
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 65
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 66
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 67
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 68
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 69
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 70
init_pop = 1
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 71
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 72
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 73
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 74
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 75
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 76
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 77
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 78
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 79
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 80
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 81
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 82
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 83
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 84
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 85
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 86
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 87
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 88
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 89
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 90
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 91
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 92
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 93
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 94
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 95
init_pop = 1
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 96
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 97
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 98
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 99
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 100
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 101
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 102
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 103
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 104
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 105
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 106
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 107
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 108
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 109
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 110
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 111
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 112
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 113
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 114
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 115
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 116
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 117
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 118
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 119
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 120
init_pop = 1
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 121
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 122
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 123
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 124
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 125
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 126
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 127
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 128
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 129
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 130
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 131
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 132
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 133
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 134
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 135
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 136
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 137
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 138
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 139
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 140
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 141
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 142
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 143
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 144
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 145
init_pop = 1
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 146
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 147
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 148
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 149
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 150
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 151
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 152
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 153
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 154
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 155
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 156
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 157
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 158
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 159
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 160
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 161
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 162
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 163
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 164
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 165
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 166
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 167
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 168
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 169
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 170
init_pop = 1
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 171
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 172
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 173
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 174
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 175
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 176
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 177
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 178
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 179
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 180
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 181
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 182
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 183
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 184
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 185
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 186
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 187
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 188
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 189
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 190
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 191
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 192
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 193
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 194
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 17

# Parameter Set 195
init_pop = 1
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 16

# Parameter Set 196
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 197
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 198
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 199
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 200
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 201
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 202
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 203
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 204
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 205
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 206
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 207
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 208
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 209
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 210
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 211
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 212
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 213
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 214
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 17

# Parameter Set 215
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 16

# Parameter Set 216
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 217
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 218
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 219
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 16

# Parameter Set 220
init_pop = 1
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 16

# Parameter Set 221
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 154

# Parameter Set 222
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 156

# Parameter Set 223
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 102

# Parameter Set 224
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 103

# Parameter Set 225
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 109

# Parameter Set 226
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 93

# Parameter Set 227
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 97

# Parameter Set 228
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 99

# Parameter Set 229
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 91

# Parameter Set 230
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 93

# Parameter Set 231
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 94

# Parameter Set 232
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 86

# Parameter Set 233
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 92

# Parameter Set 234
init_pop = 1
init_res = 11
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 93

# Parameter Set 235
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 78

# Parameter Set 236
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 82

# Parameter Set 237
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 83

# Parameter Set 238
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 84

# Parameter Set 239
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 240
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 59

# Parameter Set 241
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 60

# Parameter Set 242
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 243
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 51

# Parameter Set 244
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 245
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 246
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 247
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 248
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 51

# Parameter Set 249
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 250
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 52

# Parameter Set 251
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 252
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 253
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 254
init_pop = 1
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 255
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 47

# Parameter Set 256
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 257
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 57

# Parameter Set 258
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 60

# Parameter Set 259
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 260
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 33

# Parameter Set 261
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 262
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 263
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 264
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 265
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 266
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 267
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 268
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 269
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 270
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 271
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 272
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 273
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 274
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 275
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 276
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 277
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 278
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 279
init_pop = 1
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 280
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 281
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 282
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 283
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 47

# Parameter Set 284
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 47

# Parameter Set 285
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 286
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 287
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 288
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 289
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 290
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 291
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 292
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 293
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 294
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 295
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 296
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 297
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 298
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 299
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 300
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 301
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 302
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 303
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 304
init_pop = 1
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 305
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 306
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 307
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 308
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 309
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 310
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 311
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 312
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 313
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 314
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 315
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 316
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 317
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 318
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 319
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 320
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 321
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 322
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 323
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 324
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 325
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 326
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 327
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 328
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 329
init_pop = 1
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 330
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 331
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 332
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 333
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 334
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 335
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 336
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 337
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 338
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 339
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 340
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 341
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 342
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 343
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 344
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 345
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 346
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 347
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 348
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 349
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 350
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 351
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 352
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 353
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 354
init_pop = 1
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 355
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 356
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 357
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 358
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 359
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 360
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 361
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 362
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 363
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 364
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 365
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 366
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 367
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 368
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 369
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 370
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 371
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 372
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 373
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 374
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 375
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 376
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 377
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 378
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 379
init_pop = 1
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 380
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 381
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 382
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 383
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 384
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 385
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 386
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 387
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 388
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 389
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 390
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 391
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 392
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 393
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 394
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 395
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 396
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 397
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 398
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 399
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 400
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 401
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 402
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 403
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 404
init_pop = 1
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 405
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 406
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 407
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 408
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 409
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 410
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 411
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 412
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 413
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 414
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 415
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 416
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 417
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 418
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 419
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 420
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 421
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 422
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 423
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 424
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 425
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 426
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 427
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 428
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 429
init_pop = 1
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 430
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 170

# Parameter Set 431
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 113

# Parameter Set 432
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 112

# Parameter Set 433
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 102

# Parameter Set 434
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 102

# Parameter Set 435
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 98

# Parameter Set 436
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 98

# Parameter Set 437
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 96

# Parameter Set 438
init_pop = 1
init_res = 21
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 96

# Parameter Set 439
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 79

# Parameter Set 440
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 84

# Parameter Set 441
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 85

# Parameter Set 442
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 85

# Parameter Set 443
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 444
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 61

# Parameter Set 445
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 61

# Parameter Set 446
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 447
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 448
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 54

# Parameter Set 449
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 450
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 451
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 452
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 453
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 454
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 455
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 456
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 51

# Parameter Set 457
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 458
init_pop = 1
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 459
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 57

# Parameter Set 460
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 58

# Parameter Set 461
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 61

# Parameter Set 462
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 463
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 464
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 43

# Parameter Set 465
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 466
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 467
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 468
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 469
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 470
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 471
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 472
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 473
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 474
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 475
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 476
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 477
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 478
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 479
init_pop = 1
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 480
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 39

# Parameter Set 481
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 46

# Parameter Set 482
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 483
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 484
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 48

# Parameter Set 485
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 486
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 487
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 488
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 489
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 490
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 491
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 492
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 493
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 494
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 495
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 496
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 497
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 498
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 499
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 500
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 501
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 502
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 503
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 504
init_pop = 1
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 505
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 33

# Parameter Set 506
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 507
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 508
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 509
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 510
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 511
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 512
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 513
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 514
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 515
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 516
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 517
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 518
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 519
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 520
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 521
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 522
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 523
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 524
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 525
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 526
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 527
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 528
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 529
init_pop = 1
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 530
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 531
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 532
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 533
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 534
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 535
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 536
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 537
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 538
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 539
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 540
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 541
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 542
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 543
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 544
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 545
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 546
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 547
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 548
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 549
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 550
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 551
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 552
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 553
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 554
init_pop = 1
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 555
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 556
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 557
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 558
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 559
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 560
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 561
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 562
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 563
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 564
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 565
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 566
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 567
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 568
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 569
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 570
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 571
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 572
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 573
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 574
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 575
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 576
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 577
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 578
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 579
init_pop = 1
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 580
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 581
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 582
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 583
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 584
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 585
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 586
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 587
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 588
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 589
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 590
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 591
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 592
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 593
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 594
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 595
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 596
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 597
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 598
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 599
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 600
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 601
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 602
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 603
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 604
init_pop = 1
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 605
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 606
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 607
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 608
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 609
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 610
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 611
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 612
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 613
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 614
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 615
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 616
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 617
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 618
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 619
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 620
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 621
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 622
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 623
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 624
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 625
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 626
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 627
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 628
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 629
init_pop = 1
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 630
init_pop = 1
init_res = 31
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 132

# Parameter Set 631
init_pop = 1
init_res = 31
init_growth = 0.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 112

# Parameter Set 632
init_pop = 1
init_res = 31
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 111

# Parameter Set 633
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 87

# Parameter Set 634
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 85

# Parameter Set 635
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 85

# Parameter Set 636
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 86

# Parameter Set 637
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 62

# Parameter Set 638
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 639
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 640
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 641
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 642
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 55

# Parameter Set 643
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 644
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 645
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 646
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 54

# Parameter Set 647
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 648
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 649
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 53

# Parameter Set 650
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 52

# Parameter Set 651
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 652
init_pop = 1
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 653
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 58

# Parameter Set 654
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 61

# Parameter Set 655
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 656
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 657
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 41

# Parameter Set 658
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 43

# Parameter Set 659
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 660
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 661
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 47

# Parameter Set 662
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 663
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 664
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 665
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 666
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 667
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 668
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 669
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 670
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 671
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 672
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 673
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 674
init_pop = 1
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 675
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 40

# Parameter Set 676
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 47

# Parameter Set 677
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 678
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 679
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 48

# Parameter Set 680
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 681
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 682
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 683
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 684
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 685
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 686
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 687
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 688
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 689
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 690
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 691
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 692
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 693
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 694
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 695
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 696
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 697
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 698
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 699
init_pop = 1
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 700
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 701
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 702
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 703
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 704
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 705
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 706
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 707
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 708
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 709
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 710
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 711
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 712
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 713
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 714
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 715
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 716
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 717
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 718
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 719
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 720
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 721
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 722
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 723
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 724
init_pop = 1
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 725
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 726
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 727
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 728
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 729
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 730
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 731
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 732
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 733
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 734
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 735
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 736
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 737
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 738
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 739
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 740
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 741
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 742
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 743
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 744
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 745
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 746
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 747
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 748
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 749
init_pop = 1
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 750
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 751
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 752
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 753
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 754
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 755
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 756
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 757
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 758
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 759
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 760
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 761
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 762
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 763
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 764
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 765
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 766
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 767
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 768
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 769
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 770
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 771
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 772
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 773
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 774
init_pop = 1
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 775
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 776
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 777
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 778
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 779
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 780
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 781
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 782
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 783
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 784
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 785
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 786
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 787
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 788
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 789
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 790
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 791
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 792
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 793
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 794
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 795
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 796
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 797
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 798
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 799
init_pop = 1
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 800
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 801
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 802
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 803
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 804
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 805
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 806
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 807
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 808
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 809
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 810
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 811
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 812
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 813
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 814
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 815
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 816
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 817
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 818
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 819
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 820
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 821
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 822
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 823
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 824
init_pop = 1
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 825
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 86

# Parameter Set 826
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 86

# Parameter Set 827
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 86

# Parameter Set 828
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 63

# Parameter Set 829
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 830
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 66

# Parameter Set 831
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 832
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 60

# Parameter Set 833
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 834
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 55

# Parameter Set 835
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 836
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 837
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 838
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 839
init_pop = 1
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 840
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 49

# Parameter Set 841
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 58

# Parameter Set 842
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 61

# Parameter Set 843
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 844
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 845
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 44

# Parameter Set 846
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 847
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 848
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 48

# Parameter Set 849
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 850
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 851
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 852
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 853
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 854
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 855
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 856
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 857
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 858
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 859
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 860
init_pop = 1
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 861
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 40

# Parameter Set 862
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 47

# Parameter Set 863
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 864
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 865
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 866
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 867
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 868
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 869
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 870
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 871
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 872
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 873
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 874
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 875
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 876
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 877
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 878
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 879
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 880
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 881
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 882
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 883
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 884
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 885
init_pop = 1
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 886
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 887
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 888
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 889
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 890
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 891
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 892
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 893
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 894
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 895
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 896
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 897
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 898
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 899
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 900
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 901
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 902
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 903
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 904
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 905
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 906
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 907
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 908
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 909
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 910
init_pop = 1
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 911
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 912
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 913
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 914
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 915
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 916
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 917
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 918
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 919
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 920
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 921
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 922
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 923
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 924
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 925
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 926
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 927
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 928
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 929
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 930
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 931
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 932
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 933
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 934
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 935
init_pop = 1
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 936
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 937
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 938
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 939
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 940
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 941
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 942
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 943
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 944
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 945
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 946
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 947
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 948
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 949
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 950
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 951
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 952
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 953
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 954
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 955
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 956
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 957
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 958
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 959
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 960
init_pop = 1
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 961
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 962
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 963
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 964
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 965
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 966
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 967
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 968
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 969
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 970
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 971
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 972
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 973
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 974
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 975
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 976
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 977
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 978
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 979
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 980
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 981
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 982
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 983
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 984
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 985
init_pop = 1
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 986
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 987
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 988
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 989
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 990
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 991
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 992
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 993
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 994
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 995
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 996
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 997
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 998
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 999
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1000
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1001
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1002
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1003
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1004
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1005
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1006
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 1007
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1008
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1009
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1010
init_pop = 1
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1011
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 87

# Parameter Set 1012
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 87

# Parameter Set 1013
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 90

# Parameter Set 1014
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 64

# Parameter Set 1015
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 63

# Parameter Set 1016
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 64

# Parameter Set 1017
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 67

# Parameter Set 1018
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 60

# Parameter Set 1019
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 61

# Parameter Set 1020
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 1021
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 57

# Parameter Set 1022
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 1023
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 1024
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 69

# Parameter Set 1025
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 1026
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 1027
init_pop = 1
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 1028
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 59

# Parameter Set 1029
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 1030
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 1031
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 1032
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 44

# Parameter Set 1033
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 1034
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 1035
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 48

# Parameter Set 1036
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1037
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 1038
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 1039
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 1040
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 1041
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 1042
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1043
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1044
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 1045
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 1046
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 1047
init_pop = 1
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1048
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 40

# Parameter Set 1049
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 1050
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 1051
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1052
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1053
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1054
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1055
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 1056
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 1057
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1058
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 1059
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1060
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 1061
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1062
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1063
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1064
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1065
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1066
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1067
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1068
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1069
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1070
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1071
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 1072
init_pop = 1
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1073
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 1074
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1075
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1076
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 1077
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 1078
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1079
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1080
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1081
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 1082
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1083
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1084
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 1085
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1086
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1087
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1088
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1089
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1090
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1091
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1092
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1093
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1094
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1095
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1096
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1097
init_pop = 1
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1098
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 1099
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 1100
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1101
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1102
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1103
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1104
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1105
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1106
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1107
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1108
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1109
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1110
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1111
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 1112
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 1113
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1114
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1115
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1116
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1117
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1118
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1119
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1120
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1121
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1122
init_pop = 1
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1123
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1124
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1125
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1126
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 1127
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1128
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1129
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1130
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1131
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1132
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1133
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1134
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 1135
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1136
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1137
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1138
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1139
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1140
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1141
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1142
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1143
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1144
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1145
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1146
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1147
init_pop = 1
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1148
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1149
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1150
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1151
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1152
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1153
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1154
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1155
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1156
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1157
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1158
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1159
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1160
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1161
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1162
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1163
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1164
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1165
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1166
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1167
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 1168
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1169
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1170
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1171
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1172
init_pop = 1
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1173
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1174
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1175
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 1176
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1177
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1178
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1179
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1180
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1181
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 1182
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1183
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1184
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1185
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1186
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1187
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1188
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1189
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1190
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1191
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1192
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1193
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1194
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1195
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1196
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1197
init_pop = 1
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1198
init_pop = 1
init_res = 61
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 79

# Parameter Set 1199
init_pop = 1
init_res = 61
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 118

# Parameter Set 1200
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 82

# Parameter Set 1201
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 87

# Parameter Set 1202
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 90

# Parameter Set 1203
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 64

# Parameter Set 1204
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 68

# Parameter Set 1205
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 64

# Parameter Set 1206
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 68

# Parameter Set 1207
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 1208
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 61

# Parameter Set 1209
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 1210
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 61

# Parameter Set 1211
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 1212
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 1213
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 59

# Parameter Set 1214
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 1215
init_pop = 1
init_res = 61
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 58

# Parameter Set 1216
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 59

# Parameter Set 1217
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 1218
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1219
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 1220
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 1221
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 1222
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 1223
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1224
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1225
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 1226
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 1227
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 1228
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 1229
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 1230
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 1231
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1232
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 1233
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 1234
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 1235
init_pop = 1
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1236
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 40

# Parameter Set 1237
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 1238
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 1239
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1240
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1241
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1242
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1243
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 1244
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 1245
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1246
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 1247
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1248
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 1249
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1250
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1251
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1252
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1253
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 1254
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1255
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1256
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1257
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1258
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1259
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1260
init_pop = 1
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1261
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 1262
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 1263
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1264
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1265
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1266
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1267
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1268
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1269
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 1270
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1271
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1272
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1273
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1274
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1275
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1276
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1277
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1278
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1279
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1280
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1281
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1282
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1283
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1284
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1285
init_pop = 1
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1286
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 1287
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1288
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1289
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1290
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1291
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1292
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1293
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1294
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1295
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1296
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1297
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1298
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1299
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 1300
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 1301
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1302
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1303
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1304
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1305
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1306
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1307
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1308
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1309
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1310
init_pop = 1
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1311
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1312
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1313
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1314
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1315
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1316
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1317
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1318
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1319
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1320
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1321
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1322
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1323
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1324
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1325
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1326
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1327
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1328
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1329
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1330
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1331
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1332
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1333
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1334
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1335
init_pop = 1
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1336
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1337
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1338
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1339
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1340
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1341
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1342
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1343
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1344
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1345
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1346
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1347
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1348
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1349
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1350
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1351
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1352
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1353
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1354
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1355
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 1356
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1357
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1358
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1359
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1360
init_pop = 1
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1361
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1362
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1363
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1364
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1365
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1366
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1367
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1368
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1369
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 1370
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1371
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1372
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1373
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1374
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1375
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1376
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1377
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1378
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1379
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1380
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1381
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1382
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1383
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1384
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1385
init_pop = 1
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1386
init_pop = 1
init_res = 71
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 126

# Parameter Set 1387
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 88

# Parameter Set 1388
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 91

# Parameter Set 1389
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 68

# Parameter Set 1390
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 68

# Parameter Set 1391
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 1392
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 1393
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 1394
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 1395
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 60

# Parameter Set 1396
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 1397
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 1398
init_pop = 1
init_res = 71
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 58

# Parameter Set 1399
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 59

# Parameter Set 1400
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 62

# Parameter Set 1401
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1402
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 1403
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 36

# Parameter Set 1404
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 1405
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 1406
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 1407
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1408
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1409
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 1410
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 1411
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 1412
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 1413
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 1414
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 1415
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1416
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 1417
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1418
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1419
init_pop = 1
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1420
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 41

# Parameter Set 1421
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 1422
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 1423
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1424
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1425
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1426
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 1427
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 1428
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 1429
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 1430
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 1431
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 1432
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1433
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1434
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1435
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1436
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1437
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1438
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1439
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1440
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1441
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1442
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1443
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1444
init_pop = 1
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1445
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 1446
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 1447
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1448
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1449
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1450
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1451
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1452
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1453
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1454
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1455
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1456
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1457
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1458
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1459
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1460
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1461
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1462
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1463
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1464
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1465
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1466
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1467
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1468
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1469
init_pop = 1
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1470
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 1471
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1472
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1473
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1474
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1475
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1476
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1477
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1478
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1479
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1480
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1481
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1482
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1483
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 1484
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1485
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1486
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1487
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1488
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1489
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1490
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1491
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1492
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1493
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1494
init_pop = 1
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1495
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1496
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1497
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1498
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1499
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1500
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1501
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1502
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1503
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1504
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1505
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1506
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1507
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1508
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1509
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1510
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1511
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1512
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1513
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1514
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1515
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1516
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1517
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1518
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1519
init_pop = 1
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1520
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1521
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1522
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1523
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1524
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1525
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1526
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1527
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1528
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1529
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1530
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1531
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1532
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1533
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1534
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1535
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1536
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1537
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1538
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1539
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1540
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1541
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1542
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1543
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1544
init_pop = 1
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 1545
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1546
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1547
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1548
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1549
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1550
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1551
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1552
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1553
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 1554
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1555
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1556
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1557
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1558
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1559
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1560
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1561
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1562
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1563
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1564
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1565
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1566
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1567
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1568
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 1569
init_pop = 1
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 1570
init_pop = 1
init_res = 81
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 119

# Parameter Set 1571
init_pop = 1
init_res = 81
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 92

# Parameter Set 1572
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 92

# Parameter Set 1573
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 92

# Parameter Set 1574
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 70

# Parameter Set 1575
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 69

# Parameter Set 1576
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 69

# Parameter Set 1577
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1578
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 1579
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 61

# Parameter Set 1580
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 1581
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 1582
init_pop = 1
init_res = 81
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 1583
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 59

# Parameter Set 1584
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 63

# Parameter Set 1585
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1586
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 64

# Parameter Set 1587
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 1588
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 1589
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1590
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1591
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 1592
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1593
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 1594
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 1595
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 1596
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 1597
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 1598
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 1599
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1600
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 1601
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1602
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1603
init_pop = 1
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1604
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 41

# Parameter Set 1605
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 1606
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 1607
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1608
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1609
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1610
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 1611
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 1612
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 1613
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 1614
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 1615
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 1616
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1617
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1618
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1619
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1620
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1621
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 1622
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1623
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1624
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1625
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1626
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1627
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1628
init_pop = 1
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1629
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 1630
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 1631
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 1632
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1633
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1634
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1635
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1636
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1637
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1638
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1639
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1640
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1641
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1642
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1643
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1644
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1645
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1646
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1647
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1648
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1649
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1650
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1651
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1652
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1653
init_pop = 1
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1654
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 1655
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1656
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1657
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1658
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1659
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1660
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1661
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1662
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1663
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1664
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1665
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1666
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 1667
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 1668
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1669
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1670
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1671
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1672
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1673
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 1674
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1675
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1676
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1677
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1678
init_pop = 1
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1679
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1680
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1681
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1682
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1683
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1684
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1685
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1686
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1687
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1688
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 1689
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1690
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1691
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1692
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1693
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1694
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1695
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1696
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1697
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1698
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1699
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1700
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1701
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1702
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1703
init_pop = 1
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1704
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1705
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1706
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1707
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1708
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1709
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1710
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1711
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1712
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1713
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1714
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1715
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1716
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1717
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1718
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1719
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1720
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1721
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1722
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1723
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1724
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1725
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1726
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1727
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1728
init_pop = 1
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 1729
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1730
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1731
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1732
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1733
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1734
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1735
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1736
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1737
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 1738
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1739
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1740
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1741
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1742
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1743
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1744
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1745
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1746
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1747
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1748
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1749
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1750
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1751
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 1752
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1753
init_pop = 1
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1754
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 88

# Parameter Set 1755
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 92

# Parameter Set 1756
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 63

# Parameter Set 1757
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 72

# Parameter Set 1758
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 69

# Parameter Set 1759
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 65

# Parameter Set 1760
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 1761
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1762
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 1763
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 1764
init_pop = 1
init_res = 91
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 1765
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 60

# Parameter Set 1766
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 63

# Parameter Set 1767
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 1768
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 64

# Parameter Set 1769
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 1770
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 1771
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1772
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1773
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 1774
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 1775
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 1776
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 1777
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 1778
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 1779
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 1780
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 1781
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 1782
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 1783
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1784
init_pop = 1
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 1785
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 41

# Parameter Set 1786
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 1787
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 1788
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1789
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 1790
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 1791
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 1792
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 1793
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 1794
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 1795
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 1796
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 1797
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1798
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1799
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1800
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1801
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1802
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 1803
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1804
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1805
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1806
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1807
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1808
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1809
init_pop = 1
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1810
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 1811
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 1812
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 1813
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 42

# Parameter Set 1814
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1815
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 1816
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1817
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 1818
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1819
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1820
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1821
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1822
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1823
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1824
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1825
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1826
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1827
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1828
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1829
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1830
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1831
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1832
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1833
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1834
init_pop = 1
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1835
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 1836
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 1837
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 1838
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 1839
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 1840
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 1841
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 1842
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 1843
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 1844
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1845
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1846
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1847
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 1848
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1849
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1850
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 1851
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1852
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1853
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1854
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 1855
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1856
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1857
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1858
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1859
init_pop = 1
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 1860
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 1861
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 1862
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 1863
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1864
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 1865
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 1866
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 1867
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 1868
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 1869
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 1870
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1871
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1872
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1873
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1874
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1875
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1876
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1877
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1878
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1879
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1880
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1881
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1882
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 1883
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 1884
init_pop = 1
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1885
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 1886
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 1887
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 1888
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 1889
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 1890
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1891
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 1892
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 1893
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 1894
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 1895
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1896
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1897
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1898
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 1899
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 1900
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1901
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1902
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1903
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1904
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1905
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1906
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1907
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1908
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1909
init_pop = 1
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 1910
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 1911
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1912
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1913
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1914
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 1915
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1916
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 1917
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 1918
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 1919
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 1920
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1921
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1922
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1923
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1924
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1925
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1926
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 1927
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1928
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1929
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1930
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 1931
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 1932
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 1933
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 1934
init_pop = 1
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 1935
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 112

# Parameter Set 1936
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 122

# Parameter Set 1937
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 131

# Parameter Set 1938
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 133

# Parameter Set 1939
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 88

# Parameter Set 1940
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 87

# Parameter Set 1941
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 87

# Parameter Set 1942
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 91

# Parameter Set 1943
init_pop = 11
init_res = 1
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 84

# Parameter Set 1944
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 54

# Parameter Set 1945
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 63

# Parameter Set 1946
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 68

# Parameter Set 1947
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 71

# Parameter Set 1948
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 72

# Parameter Set 1949
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 46

# Parameter Set 1950
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 1951
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 1952
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 1953
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 46

# Parameter Set 1954
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 1955
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 1956
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 1957
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 1958
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 1959
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 1960
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 1961
init_pop = 11
init_res = 1
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 48

# Parameter Set 1962
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 39

# Parameter Set 1963
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 46

# Parameter Set 1964
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 1965
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 51

# Parameter Set 1966
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 52

# Parameter Set 1967
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 1968
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 1969
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 1970
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 1971
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 1972
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1973
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 1974
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 1975
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1976
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1977
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 1978
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1979
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1980
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 1981
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 1982
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 1983
init_pop = 11
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 1984
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 1985
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 1986
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 1987
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 1988
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 1989
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 1990
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 1991
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 1992
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 1993
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1994
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 1995
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 1996
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 1997
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 1998
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 1999
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2000
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2001
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2002
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2003
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2004
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2005
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2006
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2007
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2008
init_pop = 11
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2009
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 2010
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2011
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2012
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2013
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2014
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2015
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2016
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2017
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2018
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2019
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2020
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2021
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2022
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2023
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2024
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2025
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2026
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2027
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2028
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2029
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2030
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2031
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2032
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2033
init_pop = 11
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2034
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2035
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2036
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2037
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2038
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2039
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2040
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2041
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2042
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2043
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2044
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2045
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2046
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2047
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2048
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2049
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2050
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2051
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2052
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2053
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2054
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 2055
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2056
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2057
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2058
init_pop = 11
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2059
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2060
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2061
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2062
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2063
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2064
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2065
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2066
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2067
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2068
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2069
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2070
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2071
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2072
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2073
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2074
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2075
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2076
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2077
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2078
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2079
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2080
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 2081
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2082
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2083
init_pop = 11
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2084
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2085
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2086
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2087
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 2088
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2089
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 2090
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 2091
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2092
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2093
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2094
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2095
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 2096
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2097
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2098
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2099
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2100
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 2101
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 2102
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2103
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2104
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2105
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 2106
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 2107
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 2108
init_pop = 11
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 2109
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2110
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2111
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2112
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2113
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2114
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 2115
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 2116
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 2117
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 2118
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2119
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2120
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 2121
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 16

# Parameter Set 2122
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 2123
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 2124
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 2125
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 2126
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 16

# Parameter Set 2127
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 2128
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 2129
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 13

# Parameter Set 2130
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 2131
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 16

# Parameter Set 2132
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 17

# Parameter Set 2133
init_pop = 11
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 2134
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 134

# Parameter Set 2135
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 140

# Parameter Set 2136
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 142

# Parameter Set 2137
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 97

# Parameter Set 2138
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 97

# Parameter Set 2139
init_pop = 11
init_res = 11
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 92

# Parameter Set 2140
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 71

# Parameter Set 2141
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 75

# Parameter Set 2142
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 77

# Parameter Set 2143
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 78

# Parameter Set 2144
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 49

# Parameter Set 2145
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 2146
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 2147
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 2148
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 47

# Parameter Set 2149
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 2150
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 2151
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 2152
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 47

# Parameter Set 2153
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 2154
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 47

# Parameter Set 2155
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 2156
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 2157
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 48

# Parameter Set 2158
init_pop = 11
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 2159
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 43

# Parameter Set 2160
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 52

# Parameter Set 2161
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 2162
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 2163
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 2164
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 2165
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 2166
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 2167
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 2168
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2169
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 2170
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2171
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 2172
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2173
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 2174
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2175
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 2176
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 2177
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 2178
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2179
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 2180
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 2181
init_pop = 11
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 2182
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 2183
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 42

# Parameter Set 2184
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 2185
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 2186
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 2187
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2188
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 2189
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 2190
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 2191
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2192
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 2193
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2194
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2195
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 2196
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2197
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2198
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2199
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2200
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2201
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2202
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2203
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2204
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2205
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2206
init_pop = 11
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 2207
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 2208
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 2209
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 2210
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2211
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2212
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2213
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2214
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2215
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2216
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2217
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2218
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2219
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2220
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2221
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2222
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2223
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2224
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2225
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 2226
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2227
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2228
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2229
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2230
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 2231
init_pop = 11
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 2232
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 2233
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2234
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 2235
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2236
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 2237
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2238
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2239
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2240
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2241
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2242
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2243
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2244
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2245
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2246
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2247
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2248
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2249
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2250
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2251
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2252
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2253
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2254
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2255
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2256
init_pop = 11
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2257
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 2258
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2259
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2260
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 2261
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2262
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2263
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2264
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2265
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2266
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2267
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2268
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2269
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2270
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2271
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2272
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2273
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2274
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2275
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2276
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 2277
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2278
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2279
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2280
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2281
init_pop = 11
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 2282
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2283
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2284
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2285
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2286
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2287
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2288
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2289
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2290
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2291
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2292
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2293
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2294
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2295
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2296
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 2297
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2298
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2299
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2300
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2301
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2302
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2303
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 2304
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2305
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2306
init_pop = 11
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2307
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2308
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2309
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2310
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2311
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2312
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2313
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2314
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2315
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2316
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 2317
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2318
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2319
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2320
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2321
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2322
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2323
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 2324
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2325
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2326
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2327
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2328
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 2329
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 2330
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 2331
init_pop = 11
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 2332
init_pop = 11
init_res = 21
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 145

# Parameter Set 2333
init_pop = 11
init_res = 21
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 101

# Parameter Set 2334
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 73

# Parameter Set 2335
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 77

# Parameter Set 2336
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 78

# Parameter Set 2337
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 79

# Parameter Set 2338
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 2339
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 55

# Parameter Set 2340
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 2341
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 2342
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 2343
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 2344
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 2345
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 2346
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 2347
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 2348
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 2349
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 2350
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 2351
init_pop = 11
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 2352
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 53

# Parameter Set 2353
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 54

# Parameter Set 2354
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 2355
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 2356
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 2357
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 2358
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 2359
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 2360
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 2361
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 2362
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 2363
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 2364
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2365
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2366
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 2367
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2368
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 2369
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2370
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 2371
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 2372
init_pop = 11
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 2373
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 36

# Parameter Set 2374
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 43

# Parameter Set 2375
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 2376
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 2377
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 2378
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 2379
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2380
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2381
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2382
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 2383
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2384
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2385
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 2386
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2387
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2388
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2389
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2390
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2391
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 2392
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2393
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2394
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2395
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2396
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 2397
init_pop = 11
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2398
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 2399
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 2400
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 2401
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 2402
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2403
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2404
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2405
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2406
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2407
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2408
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2409
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2410
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2411
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2412
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2413
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2414
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2415
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2416
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2417
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2418
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2419
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2420
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2421
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 2422
init_pop = 11
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2423
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 2424
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2425
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2426
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2427
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 2428
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2429
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2430
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2431
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2432
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2433
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2434
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2435
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2436
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2437
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 2438
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2439
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2440
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2441
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2442
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2443
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2444
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2445
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2446
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2447
init_pop = 11
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2448
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 2449
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2450
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2451
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2452
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2453
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2454
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2455
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2456
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2457
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2458
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2459
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2460
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2461
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2462
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2463
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2464
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2465
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2466
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2467
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2468
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2469
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2470
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2471
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2472
init_pop = 11
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2473
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2474
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2475
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2476
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2477
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2478
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2479
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2480
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2481
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2482
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2483
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2484
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2485
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2486
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2487
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2488
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2489
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2490
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2491
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2492
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 2493
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2494
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2495
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2496
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2497
init_pop = 11
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2498
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2499
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2500
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2501
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 2502
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2503
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2504
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2505
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2506
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2507
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2508
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2509
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2510
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2511
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2512
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2513
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2514
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2515
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2516
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2517
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2518
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 2519
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 2520
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2521
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2522
init_pop = 11
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2523
init_pop = 11
init_res = 31
init_growth = 0.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 84

# Parameter Set 2524
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 80

# Parameter Set 2525
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 79

# Parameter Set 2526
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 79

# Parameter Set 2527
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 80

# Parameter Set 2528
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 2529
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 2530
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 2531
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 2532
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 50

# Parameter Set 2533
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 2534
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 2535
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 2536
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 51

# Parameter Set 2537
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 52

# Parameter Set 2538
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 50

# Parameter Set 2539
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 2540
init_pop = 11
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 2541
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 2542
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 57

# Parameter Set 2543
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 2544
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 58

# Parameter Set 2545
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 2546
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 2547
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 2548
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 2549
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 2550
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 2551
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 2552
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2553
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 2554
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 2555
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2556
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2557
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2558
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 2559
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 2560
init_pop = 11
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 2561
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 37

# Parameter Set 2562
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 44

# Parameter Set 2563
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 2564
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 2565
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 2566
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 2567
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 2568
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2569
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2570
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2571
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 2572
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2573
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 2574
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 2575
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2576
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2577
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2578
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2579
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2580
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2581
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2582
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2583
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2584
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 2585
init_pop = 11
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2586
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 2587
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 2588
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 2589
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 2590
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2591
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2592
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2593
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2594
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2595
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 2596
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2597
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2598
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2599
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2600
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2601
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2602
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2603
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2604
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2605
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2606
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2607
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2608
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 2609
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2610
init_pop = 11
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2611
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 2612
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2613
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2614
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2615
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2616
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2617
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2618
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2619
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2620
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2621
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2622
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2623
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2624
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2625
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2626
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2627
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2628
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2629
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2630
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2631
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2632
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2633
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2634
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2635
init_pop = 11
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2636
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 2637
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2638
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2639
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2640
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2641
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2642
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2643
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2644
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2645
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2646
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2647
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2648
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2649
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2650
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2651
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2652
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2653
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2654
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2655
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2656
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2657
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2658
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2659
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2660
init_pop = 11
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2661
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2662
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2663
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2664
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2665
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2666
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2667
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2668
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2669
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2670
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2671
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2672
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2673
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2674
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2675
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2676
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2677
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2678
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2679
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2680
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2681
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2682
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2683
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2684
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2685
init_pop = 11
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2686
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2687
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2688
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2689
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2690
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2691
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2692
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2693
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2694
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2695
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2696
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2697
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2698
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2699
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2700
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2701
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2702
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2703
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2704
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2705
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2706
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2707
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2708
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2709
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 2710
init_pop = 11
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 2711
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 58

# Parameter Set 2712
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 80

# Parameter Set 2713
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 80

# Parameter Set 2714
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 80

# Parameter Set 2715
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 57

# Parameter Set 2716
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 2717
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 2718
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 54

# Parameter Set 2719
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 2720
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 2721
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 51

# Parameter Set 2722
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 2723
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 2724
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 2725
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 51

# Parameter Set 2726
init_pop = 11
init_res = 41
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 2727
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 2728
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 57

# Parameter Set 2729
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 2730
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 58

# Parameter Set 2731
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 2732
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 2733
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 2734
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 2735
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 2736
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 2737
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 2738
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 2739
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 2740
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 2741
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 2742
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2743
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 2744
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 2745
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2746
init_pop = 11
init_res = 41
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 2747
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 37

# Parameter Set 2748
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 44

# Parameter Set 2749
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 2750
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 2751
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 2752
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 2753
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2754
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 2755
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 2756
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2757
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2758
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2759
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 2760
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 2761
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 2762
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2763
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2764
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2765
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2766
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2767
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2768
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2769
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2770
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 2771
init_pop = 11
init_res = 41
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2772
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 2773
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 2774
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 2775
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 2776
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2777
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 2778
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2779
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2780
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 2781
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2782
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2783
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2784
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2785
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2786
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2787
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2788
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2789
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2790
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2791
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2792
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2793
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2794
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2795
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2796
init_pop = 11
init_res = 41
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2797
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 2798
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2799
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 2800
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 2801
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2802
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2803
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2804
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2805
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2806
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2807
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2808
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2809
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2810
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2811
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2812
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2813
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2814
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2815
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2816
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2817
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2818
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2819
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2820
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2821
init_pop = 11
init_res = 41
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2822
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 2823
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 2824
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2825
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 2826
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2827
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2828
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2829
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2830
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 2831
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 2832
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2833
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 2834
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2835
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2836
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2837
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2838
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2839
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2840
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2841
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2842
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2843
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2844
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 2845
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2846
init_pop = 11
init_res = 41
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2847
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2848
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2849
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2850
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 2851
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 2852
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2853
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2854
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 2855
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 2856
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 2857
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2858
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2859
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2860
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 2861
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2862
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2863
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2864
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2865
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2866
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2867
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2868
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2869
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2870
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2871
init_pop = 11
init_res = 41
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2872
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2873
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 2874
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2875
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2876
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2877
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 2878
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 2879
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 2880
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 2881
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 2882
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2883
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2884
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2885
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2886
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2887
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2888
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 2889
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 2890
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2891
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2892
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 2893
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 2894
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 2895
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 2896
init_pop = 11
init_res = 41
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 2897
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 80

# Parameter Set 2898
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 81

# Parameter Set 2899
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 81

# Parameter Set 2900
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 58

# Parameter Set 2901
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 2902
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 61

# Parameter Set 2903
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 2904
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 2905
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 2906
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 2907
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 2908
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 2909
init_pop = 11
init_res = 51
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 52

# Parameter Set 2910
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 55

# Parameter Set 2911
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 58

# Parameter Set 2912
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 2913
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 2914
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 40

# Parameter Set 2915
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 2916
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 2917
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 2918
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 2919
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 2920
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 2921
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 2922
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 2923
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 2924
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 2925
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 2926
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2927
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 2928
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 2929
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 2930
init_pop = 11
init_res = 51
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 2931
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 37

# Parameter Set 2932
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 2933
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 45

# Parameter Set 2934
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 46

# Parameter Set 2935
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 2936
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 2937
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2938
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 2939
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 2940
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2941
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 2942
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2943
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 2944
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 2945
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 2946
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 2947
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 2948
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 2949
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 2950
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 2951
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2952
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2953
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 2954
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2955
init_pop = 11
init_res = 51
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2956
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 2957
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 2958
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 2959
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 2960
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 2961
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 2962
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 2963
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 2964
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 2965
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 2966
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2967
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 2968
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 2969
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 2970
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 2971
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2972
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2973
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2974
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2975
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2976
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2977
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2978
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 2979
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2980
init_pop = 11
init_res = 51
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2981
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 2982
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 2983
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 2984
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 2985
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 2986
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 2987
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 2988
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 2989
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 2990
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 2991
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 2992
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 2993
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2994
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 2995
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 2996
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 2997
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 2998
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 2999
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3000
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3001
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3002
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3003
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3004
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3005
init_pop = 11
init_res = 51
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3006
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3007
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3008
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3009
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3010
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3011
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3012
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3013
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3014
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3015
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3016
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3017
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3018
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3019
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3020
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3021
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3022
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3023
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3024
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3025
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3026
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3027
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3028
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3029
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3030
init_pop = 11
init_res = 51
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3031
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3032
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3033
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3034
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3035
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3036
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3037
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3038
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3039
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3040
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3041
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3042
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3043
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3044
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3045
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3046
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3047
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3048
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3049
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3050
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3051
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3052
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3053
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3054
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3055
init_pop = 11
init_res = 51
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3056
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3057
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 3058
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3059
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3060
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3061
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3062
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3063
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3064
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3065
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3066
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3067
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3068
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3069
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3070
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3071
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3072
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3073
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3074
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3075
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3076
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3077
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3078
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3079
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3080
init_pop = 11
init_res = 51
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3081
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 86

# Parameter Set 3082
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 81

# Parameter Set 3083
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 84

# Parameter Set 3084
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 58

# Parameter Set 3085
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 3086
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 3087
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 3088
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 3089
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 3090
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 3091
init_pop = 11
init_res = 61
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 3092
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 55

# Parameter Set 3093
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 58

# Parameter Set 3094
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 3095
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 3096
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 3097
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 41

# Parameter Set 3098
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 3099
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 3100
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 3101
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3102
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 3103
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3104
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3105
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 3106
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3107
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3108
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 3109
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3110
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 3111
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 3112
init_pop = 11
init_res = 61
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 3113
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 3114
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 3115
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 3116
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 46

# Parameter Set 3117
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 3118
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 3119
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 3120
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3121
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 3122
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 3123
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3124
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3125
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3126
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 3127
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3128
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3129
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3130
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 3131
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3132
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3133
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3134
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3135
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3136
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3137
init_pop = 11
init_res = 61
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 3138
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 3139
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 3140
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3141
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3142
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3143
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3144
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3145
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3146
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3147
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 3148
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3149
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3150
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3151
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3152
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3153
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3154
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3155
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3156
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3157
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3158
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3159
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3160
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3161
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3162
init_pop = 11
init_res = 61
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3163
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 3164
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3165
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3166
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 3167
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 3168
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3169
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3170
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3171
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3172
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3173
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3174
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3175
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3176
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3177
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 3178
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3179
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3180
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3181
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3182
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3183
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3184
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3185
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3186
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3187
init_pop = 11
init_res = 61
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3188
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3189
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3190
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3191
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3192
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3193
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3194
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3195
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3196
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3197
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3198
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3199
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3200
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3201
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3202
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3203
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3204
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3205
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3206
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3207
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3208
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3209
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3210
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3211
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3212
init_pop = 11
init_res = 61
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3213
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3214
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3215
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3216
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3217
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3218
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3219
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3220
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3221
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3222
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3223
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3224
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3225
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3226
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3227
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3228
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3229
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3230
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3231
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3232
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3233
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3234
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3235
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3236
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3237
init_pop = 11
init_res = 61
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3238
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3239
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 3240
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3241
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3242
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3243
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3244
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3245
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3246
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3247
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3248
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3249
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3250
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3251
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3252
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3253
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3254
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3255
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3256
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3257
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3258
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3259
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3260
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3261
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3262
init_pop = 11
init_res = 61
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3263
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 82

# Parameter Set 3264
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 85

# Parameter Set 3265
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 62

# Parameter Set 3266
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 62

# Parameter Set 3267
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 51

# Parameter Set 3268
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 56

# Parameter Set 3269
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 3270
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 3271
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 3272
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 3273
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 3274
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 3275
init_pop = 11
init_res = 71
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 3276
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 55

# Parameter Set 3277
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 58

# Parameter Set 3278
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 3279
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 59

# Parameter Set 3280
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 3281
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 3282
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 3283
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 3284
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 3285
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 3286
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 3287
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3288
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3289
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 3290
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3291
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3292
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3293
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 3294
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 3295
init_pop = 11
init_res = 71
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 3296
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 3297
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 3298
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 3299
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 46

# Parameter Set 3300
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 3301
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 3302
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3303
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3304
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 3305
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 3306
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3307
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3308
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 3309
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 3310
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3311
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3312
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3313
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 3314
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3315
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3316
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3317
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3318
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3319
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3320
init_pop = 11
init_res = 71
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3321
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 3322
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 3323
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3324
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3325
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3326
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3327
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3328
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3329
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3330
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3331
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3332
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3333
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3334
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3335
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3336
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3337
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3338
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3339
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3340
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3341
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3342
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3343
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3344
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3345
init_pop = 11
init_res = 71
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3346
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 3347
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3348
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3349
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 3350
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 3351
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3352
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3353
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3354
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3355
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3356
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3357
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3358
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3359
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3360
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3361
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3362
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3363
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3364
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3365
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3366
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3367
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3368
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3369
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3370
init_pop = 11
init_res = 71
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3371
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3372
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3373
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3374
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3375
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3376
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3377
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3378
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3379
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 3380
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3381
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3382
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3383
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3384
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3385
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3386
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3387
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3388
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3389
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3390
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3391
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3392
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3393
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3394
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3395
init_pop = 11
init_res = 71
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3396
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3397
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3398
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3399
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3400
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3401
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3402
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3403
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3404
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3405
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3406
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3407
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3408
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3409
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3410
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3411
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3412
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3413
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3414
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3415
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3416
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3417
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3418
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3419
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3420
init_pop = 11
init_res = 71
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3421
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 3422
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 3423
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3424
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3425
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3426
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3427
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3428
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3429
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3430
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3431
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3432
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3433
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3434
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3435
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3436
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3437
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3438
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3439
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3440
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3441
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3442
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3443
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3444
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3445
init_pop = 11
init_res = 71
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3446
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 85

# Parameter Set 3447
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 85

# Parameter Set 3448
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 63

# Parameter Set 3449
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 3450
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 3451
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 3452
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 57

# Parameter Set 3453
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 3454
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 61

# Parameter Set 3455
init_pop = 11
init_res = 81
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 3456
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 46

# Parameter Set 3457
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 55

# Parameter Set 3458
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 59

# Parameter Set 3459
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 3460
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 3461
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 3462
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 3463
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 3464
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 3465
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 3466
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 3467
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 3468
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 3469
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 3470
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3471
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 3472
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3473
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3474
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3475
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 3476
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 3477
init_pop = 11
init_res = 81
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3478
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 3479
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 3480
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 3481
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 46

# Parameter Set 3482
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 46

# Parameter Set 3483
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 3484
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3485
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3486
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3487
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 3488
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3489
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3490
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 3491
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 3492
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 3493
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3494
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3495
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 3496
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3497
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3498
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3499
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3500
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3501
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3502
init_pop = 11
init_res = 81
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3503
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 3504
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 3505
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3506
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3507
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3508
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3509
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3510
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3511
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3512
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3513
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3514
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3515
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3516
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3517
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3518
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3519
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3520
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3521
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3522
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3523
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3524
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3525
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3526
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3527
init_pop = 11
init_res = 81
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3528
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 3529
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3530
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3531
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 3532
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 3533
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3534
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3535
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3536
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3537
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3538
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3539
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3540
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 3541
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3542
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3543
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3544
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3545
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3546
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3547
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3548
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3549
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3550
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3551
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3552
init_pop = 11
init_res = 81
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3553
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3554
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3555
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3556
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3557
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3558
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3559
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3560
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 3561
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 3562
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3563
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3564
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3565
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3566
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3567
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3568
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3569
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3570
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3571
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3572
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3573
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3574
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3575
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3576
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3577
init_pop = 11
init_res = 81
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3578
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3579
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3580
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3581
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3582
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3583
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3584
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3585
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3586
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3587
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3588
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3589
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3590
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3591
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3592
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3593
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3594
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3595
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3596
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3597
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3598
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3599
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3600
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3601
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3602
init_pop = 11
init_res = 81
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3603
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3604
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3605
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3606
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3607
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3608
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3609
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3610
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3611
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3612
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3613
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3614
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3615
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3616
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3617
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3618
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3619
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3620
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3621
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3622
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3623
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3624
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3625
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3626
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3627
init_pop = 11
init_res = 81
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3628
init_pop = 11
init_res = 91
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 82

# Parameter Set 3629
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 90

# Parameter Set 3630
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 86

# Parameter Set 3631
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 74

# Parameter Set 3632
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 63

# Parameter Set 3633
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 3634
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 3635
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 60

# Parameter Set 3636
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 3637
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 3638
init_pop = 11
init_res = 91
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 3639
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 56

# Parameter Set 3640
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 59

# Parameter Set 3641
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 59

# Parameter Set 3642
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 60

# Parameter Set 3643
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 3644
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 3645
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 45

# Parameter Set 3646
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 45

# Parameter Set 3647
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 3648
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 40

# Parameter Set 3649
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 41

# Parameter Set 3650
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 41

# Parameter Set 3651
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 3652
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3653
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 3654
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3655
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 3656
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3657
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 3658
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 3659
init_pop = 11
init_res = 91
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3660
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 3661
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 45

# Parameter Set 3662
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 3663
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 46

# Parameter Set 3664
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 47

# Parameter Set 3665
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3666
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3667
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 3668
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3669
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 3670
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3671
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3672
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 3673
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 3674
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 34

# Parameter Set 3675
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 3676
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3677
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3678
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3679
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3680
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3681
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3682
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 3683
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3684
init_pop = 11
init_res = 91
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3685
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 32

# Parameter Set 3686
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 39

# Parameter Set 3687
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 3688
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 3689
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 40

# Parameter Set 3690
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 3691
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3692
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3693
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 3694
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 3695
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3696
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3697
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3698
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3699
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3700
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3701
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3702
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3703
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3704
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3705
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3706
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3707
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3708
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3709
init_pop = 11
init_res = 91
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3710
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 3711
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3712
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3713
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3714
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 3715
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 3716
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3717
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3718
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3719
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3720
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3721
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3722
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 3723
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 3724
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3725
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3726
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3727
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3728
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3729
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3730
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3731
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3732
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3733
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3734
init_pop = 11
init_res = 91
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3735
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 3736
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 3737
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3738
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3739
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3740
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3741
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3742
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 3743
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 3744
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3745
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3746
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3747
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3748
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3749
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3750
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3751
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3752
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3753
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3754
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3755
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3756
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3757
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3758
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3759
init_pop = 11
init_res = 91
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3760
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3761
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 3762
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3763
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3764
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3765
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3766
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3767
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3768
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3769
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3770
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3771
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3772
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3773
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3774
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3775
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3776
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3777
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3778
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3779
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3780
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3781
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3782
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3783
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3784
init_pop = 11
init_res = 91
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3785
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 3786
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3787
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3788
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3789
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3790
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3791
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3792
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3793
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3794
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3795
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3796
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 3797
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3798
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3799
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3800
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3801
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3802
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3803
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3804
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3805
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 3806
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3807
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3808
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 3809
init_pop = 11
init_res = 91
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3810
init_pop = 21
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 108

# Parameter Set 3811
init_pop = 21
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 117

# Parameter Set 3812
init_pop = 21
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 121

# Parameter Set 3813
init_pop = 21
init_res = 1
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 129

# Parameter Set 3814
init_pop = 21
init_res = 1
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 95

# Parameter Set 3815
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 54

# Parameter Set 3816
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 61

# Parameter Set 3817
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 63

# Parameter Set 3818
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 68

# Parameter Set 3819
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 70

# Parameter Set 3820
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 50

# Parameter Set 3821
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 50

# Parameter Set 3822
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 51

# Parameter Set 3823
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 3824
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 3825
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 3826
init_pop = 21
init_res = 1
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 3827
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 38

# Parameter Set 3828
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 44

# Parameter Set 3829
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 46

# Parameter Set 3830
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 47

# Parameter Set 3831
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 3832
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 3833
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 3834
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 3835
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 3836
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3837
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 3838
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3839
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 3840
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 3841
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 3842
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3843
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 3844
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 3845
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 3846
init_pop = 21
init_res = 1
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 3847
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 3848
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 3849
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 3850
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 3851
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 3852
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 3853
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 3854
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 3855
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3856
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3857
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3858
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3859
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3860
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 3861
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 3862
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3863
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 3864
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3865
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3866
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3867
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 3868
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 3869
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 3870
init_pop = 21
init_res = 1
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 3871
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 3872
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 3873
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 3874
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 3875
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 3876
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 3877
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 3878
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3879
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3880
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3881
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3882
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3883
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 3884
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3885
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 3886
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 3887
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3888
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3889
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 3890
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3891
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 3892
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3893
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3894
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3895
init_pop = 21
init_res = 1
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 3896
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 3897
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 3898
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 3899
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 3900
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 3901
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 3902
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3903
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3904
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3905
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3906
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 3907
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3908
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3909
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3910
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3911
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 3912
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3913
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3914
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3915
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3916
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 3917
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3918
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 3919
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 3920
init_pop = 21
init_res = 1
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3921
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 3922
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 3923
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 3924
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 3925
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 3926
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 3927
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 3928
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 3929
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 3930
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 3931
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3932
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3933
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 3934
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3935
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3936
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3937
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3938
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 3939
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3940
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 3941
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 13

# Parameter Set 3942
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 3943
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 3944
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3945
init_pop = 21
init_res = 1
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 3946
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3947
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 3948
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 3949
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 3950
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 3951
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 3952
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 3953
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 3954
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3955
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 3956
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3957
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 3958
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 3959
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3960
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 3961
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3962
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 3963
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 3964
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 3965
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 3966
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 13

# Parameter Set 3967
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 3968
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 3969
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 3970
init_pop = 21
init_res = 1
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 3971
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 3972
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 3973
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 3974
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 3975
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 3976
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 3977
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 3978
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 3979
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 3980
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 3981
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3982
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 3983
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 3984
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 3985
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 3986
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 14

# Parameter Set 3987
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 3988
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 3989
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 3990
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 3991
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 13

# Parameter Set 3992
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 16

# Parameter Set 3993
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 17

# Parameter Set 3994
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 3995
init_pop = 21
init_res = 1
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 3996
init_pop = 21
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 130

# Parameter Set 3997
init_pop = 21
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 136

# Parameter Set 3998
init_pop = 21
init_res = 11
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 138

# Parameter Set 3999
init_pop = 21
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 99

# Parameter Set 4000
init_pop = 21
init_res = 11
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 97

# Parameter Set 4001
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 70

# Parameter Set 4002
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 74

# Parameter Set 4003
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 75

# Parameter Set 4004
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 76

# Parameter Set 4005
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 48

# Parameter Set 4006
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 52

# Parameter Set 4007
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 4008
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 4009
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 47

# Parameter Set 4010
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 51

# Parameter Set 4011
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 4012
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 4013
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 4014
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 4015
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 4016
init_pop = 21
init_res = 11
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 49

# Parameter Set 4017
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 42

# Parameter Set 4018
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 51

# Parameter Set 4019
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 52

# Parameter Set 4020
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 4021
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 4022
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 4023
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 4024
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 38

# Parameter Set 4025
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 4026
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 4027
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 4028
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 4029
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 4030
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 4031
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4032
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 4033
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 4034
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 4035
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 4036
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 4037
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 34

# Parameter Set 4038
init_pop = 21
init_res = 11
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 35

# Parameter Set 4039
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 34

# Parameter Set 4040
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 41

# Parameter Set 4041
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 42

# Parameter Set 4042
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 43

# Parameter Set 4043
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 43

# Parameter Set 4044
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4045
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 30

# Parameter Set 4046
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 4047
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 4048
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 4049
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 4050
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4051
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 4052
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 4053
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 4054
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4055
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 4056
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 4057
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 4058
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 4059
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4060
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 4061
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 4062
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 4063
init_pop = 21
init_res = 11
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 4064
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 29

# Parameter Set 4065
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 35

# Parameter Set 4066
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 4067
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 4068
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 4069
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4070
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 4071
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 4072
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 4073
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 4074
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4075
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 4076
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4077
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4078
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4079
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4080
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4081
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 4082
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 4083
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4084
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4085
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4086
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 4087
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 4088
init_pop = 21
init_res = 11
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4089
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 4090
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 4091
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 4092
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 4093
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 4094
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4095
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4096
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4097
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 4098
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4099
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4100
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4101
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4102
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4103
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 24

# Parameter Set 4104
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4105
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4106
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4107
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4108
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4109
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4110
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4111
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4112
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4113
init_pop = 21
init_res = 11
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4114
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 25

# Parameter Set 4115
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 4116
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4117
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 4118
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 4119
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4120
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4121
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4122
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4123
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4124
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4125
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4126
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4127
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4128
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4129
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4130
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4131
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4132
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4133
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4134
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 4135
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4136
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4137
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4138
init_pop = 21
init_res = 11
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 4139
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4140
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 4141
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 4142
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 4143
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 4144
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4145
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4146
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4147
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4148
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4149
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4150
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4151
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4152
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4153
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4154
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4155
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4156
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 4157
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 4158
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 4159
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 4160
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4161
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 4162
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 4163
init_pop = 21
init_res = 11
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4164
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 4165
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 4166
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 4167
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 24

# Parameter Set 4168
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4169
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4170
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4171
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4172
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4173
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4174
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4175
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4176
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4177
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4178
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4179
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4180
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4181
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 4182
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 4183
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 4184
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 15

# Parameter Set 4185
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 17

# Parameter Set 4186
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 4187
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 18

# Parameter Set 4188
init_pop = 21
init_res = 11
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 18

# Parameter Set 4189
init_pop = 21
init_res = 21
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 142

# Parameter Set 4190
init_pop = 21
init_res = 21
init_growth = 0.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 141

# Parameter Set 4191
init_pop = 21
init_res = 21
init_growth = 0.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 87

# Parameter Set 4192
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 72

# Parameter Set 4193
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 76

# Parameter Set 4194
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 77

# Parameter Set 4195
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 77

# Parameter Set 4196
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 54

# Parameter Set 4197
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 54

# Parameter Set 4198
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 54

# Parameter Set 4199
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 54

# Parameter Set 4200
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 48

# Parameter Set 4201
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 52

# Parameter Set 4202
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 52

# Parameter Set 4203
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 49

# Parameter Set 4204
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 4205
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 4206
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 49

# Parameter Set 4207
init_pop = 21
init_res = 21
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 4208
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 49

# Parameter Set 4209
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 52

# Parameter Set 4210
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 4211
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 4212
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 56

# Parameter Set 4213
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 4214
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 4215
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 39

# Parameter Set 4216
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 39

# Parameter Set 4217
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 4218
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 4219
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 4220
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 4221
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 28

# Parameter Set 4222
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4223
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 4224
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 4225
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 4226
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 4227
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4228
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 34

# Parameter Set 4229
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 35

# Parameter Set 4230
init_pop = 21
init_res = 21
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 4231
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 35

# Parameter Set 4232
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 42

# Parameter Set 4233
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 43

# Parameter Set 4234
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 4235
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 4236
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 4237
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 31

# Parameter Set 4238
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 4239
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 32

# Parameter Set 4240
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 32

# Parameter Set 4241
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 22

# Parameter Set 4242
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4243
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 30

# Parameter Set 4244
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 4245
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 4246
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4247
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4248
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4249
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 4250
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 4251
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4252
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 4253
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4254
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 4255
init_pop = 21
init_res = 21
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 4256
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 30

# Parameter Set 4257
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 36

# Parameter Set 4258
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 4259
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 4260
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 4261
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4262
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4263
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 4264
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 4265
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 29

# Parameter Set 4266
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4267
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 4268
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 4269
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4270
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4271
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4272
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4273
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4274
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4275
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4276
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4277
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4278
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 24

# Parameter Set 4279
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 4280
init_pop = 21
init_res = 21
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4281
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 4282
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4283
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 4284
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 4285
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 4286
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4287
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4288
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4289
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4290
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4291
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4292
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4293
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 4294
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 4295
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4296
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4297
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4298
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4299
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4300
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4301
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4302
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4303
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4304
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4305
init_pop = 21
init_res = 21
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4306
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 4307
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 4308
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 4309
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 4310
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 4311
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4312
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4313
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 4314
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 4315
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 4316
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4317
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4318
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4319
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4320
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4321
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4322
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4323
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4324
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4325
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4326
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4327
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4328
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4329
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4330
init_pop = 21
init_res = 21
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4331
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4332
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4333
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 27

# Parameter Set 4334
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 4335
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 4336
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4337
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4338
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4339
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4340
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4341
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4342
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4343
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4344
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4345
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4346
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4347
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4348
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4349
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4350
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4351
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4352
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4353
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4354
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4355
init_pop = 21
init_res = 21
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4356
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4357
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 4358
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4359
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4360
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4361
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4362
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4363
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4364
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4365
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4366
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4367
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4368
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4369
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4370
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4371
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4372
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4373
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4374
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4375
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4376
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4377
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 18

# Parameter Set 4378
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 18

# Parameter Set 4379
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4380
init_pop = 21
init_res = 21
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4381
init_pop = 21
init_res = 31
init_growth = 0.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 147

# Parameter Set 4382
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 77

# Parameter Set 4383
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 77

# Parameter Set 4384
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 78

# Parameter Set 4385
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 78

# Parameter Set 4386
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 55

# Parameter Set 4387
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 55

# Parameter Set 4388
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 55

# Parameter Set 4389
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 52

# Parameter Set 4390
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 53

# Parameter Set 4391
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 53

# Parameter Set 4392
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 4393
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 51

# Parameter Set 4394
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 50

# Parameter Set 4395
init_pop = 21
init_res = 31
init_growth = 0.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 50

# Parameter Set 4396
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 51

# Parameter Set 4397
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 53

# Parameter Set 4398
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 53

# Parameter Set 4399
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 56

# Parameter Set 4400
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 57

# Parameter Set 4401
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 38

# Parameter Set 4402
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 39

# Parameter Set 4403
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 40

# Parameter Set 4404
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 42

# Parameter Set 4405
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 34

# Parameter Set 4406
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 4407
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 4408
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 4409
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 33

# Parameter Set 4410
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 36

# Parameter Set 4411
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 37

# Parameter Set 4412
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 37

# Parameter Set 4413
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4414
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 35

# Parameter Set 4415
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 36

# Parameter Set 4416
init_pop = 21
init_res = 31
init_growth = 0.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 36

# Parameter Set 4417
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 36

# Parameter Set 4418
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 43

# Parameter Set 4419
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 44

# Parameter Set 4420
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 44

# Parameter Set 4421
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 44

# Parameter Set 4422
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 4423
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4424
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 32

# Parameter Set 4425
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 4426
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 4427
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4428
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 28

# Parameter Set 4429
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 31

# Parameter Set 4430
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 4431
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 4432
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4433
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4434
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4435
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 30

# Parameter Set 4436
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 4437
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4438
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4439
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4440
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 29

# Parameter Set 4441
init_pop = 21
init_res = 31
init_growth = 0.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 4442
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 31

# Parameter Set 4443
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 37

# Parameter Set 4444
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 37

# Parameter Set 4445
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 38

# Parameter Set 4446
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 38

# Parameter Set 4447
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 21

# Parameter Set 4448
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4449
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4450
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 4451
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 30

# Parameter Set 4452
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4453
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 26

# Parameter Set 4454
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 4455
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 4456
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 4457
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4458
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4459
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 4460
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4461
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4462
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4463
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4464
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4465
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 4466
init_pop = 21
init_res = 31
init_growth = 1.01
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4467
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 27

# Parameter Set 4468
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 32

# Parameter Set 4469
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 33

# Parameter Set 4470
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 33

# Parameter Set 4471
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 33

# Parameter Set 4472
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4473
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 24

# Parameter Set 4474
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 26

# Parameter Set 4475
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 26

# Parameter Set 4476
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 26

# Parameter Set 4477
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 19

# Parameter Set 4478
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4479
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 4480
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 25

# Parameter Set 4481
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 25

# Parameter Set 4482
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4483
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4484
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4485
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 4486
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 4487
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4488
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4489
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4490
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4491
init_pop = 21
init_res = 31
init_growth = 1.21
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4492
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 26

# Parameter Set 4493
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 29

# Parameter Set 4494
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 29

# Parameter Set 4495
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 31

# Parameter Set 4496
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 31

# Parameter Set 4497
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 20

# Parameter Set 4498
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 23

# Parameter Set 4499
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 23

# Parameter Set 4500
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 4501
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 4502
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4503
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 22

# Parameter Set 4504
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4505
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4506
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4507
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4508
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4509
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4510
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 22

# Parameter Set 4511
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4512
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4513
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4514
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 21

# Parameter Set 4515
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4516
init_pop = 21
init_res = 31
init_growth = 1.41
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4517
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 24

# Parameter Set 4518
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 27

# Parameter Set 4519
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 28

# Parameter Set 4520
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 28

# Parameter Set 4521
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 28

# Parameter Set 4522
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4523
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 21

# Parameter Set 4524
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 22

# Parameter Set 4525
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 23

# Parameter Set 4526
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 23

# Parameter Set 4527
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4528
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4529
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4530
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 21

# Parameter Set 4531
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4532
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4533
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4534
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4535
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4536
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 21

# Parameter Set 4537
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4538
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4539
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4540
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4541
init_pop = 21
init_res = 31
init_growth = 1.61
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 4542
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.01
dt = 0.01
simulation_time = 23

# Parameter Set 4543
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.21
dt = 0.01
simulation_time = 25

# Parameter Set 4544
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.41
dt = 0.01
simulation_time = 25

# Parameter Set 4545
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.61
dt = 0.01
simulation_time = 27

# Parameter Set 4546
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.01
init_replenishment = 0.81
dt = 0.01
simulation_time = 27

# Parameter Set 4547
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4548
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4549
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4550
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4551
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.21
init_replenishment = 0.81
dt = 0.01
simulation_time = 22

# Parameter Set 4552
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.01
dt = 0.01
simulation_time = 18

# Parameter Set 4553
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.21
dt = 0.01
simulation_time = 20

# Parameter Set 4554
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.41
dt = 0.01
simulation_time = 20

# Parameter Set 4555
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.61
dt = 0.01
simulation_time = 20

# Parameter Set 4556
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.41
init_replenishment = 0.81
dt = 0.01
simulation_time = 20

# Parameter Set 4557
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.01
dt = 0.01
simulation_time = 17

# Parameter Set 4558
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4559
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4560
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4561
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.61
init_replenishment = 0.81
dt = 0.01
simulation_time = 19

# Parameter Set 4562
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.01
dt = 0.01
simulation_time = 16

# Parameter Set 4563
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.21
dt = 0.01
simulation_time = 19

# Parameter Set 4564
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.41
dt = 0.01
simulation_time = 19

# Parameter Set 4565
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.61
dt = 0.01
simulation_time = 19

# Parameter Set 4566
init_pop = 21
init_res = 31
init_growth = 1.81
init_consumption = 0.81
init_replenishment = 0.81
dt = 0.01
simulation_time = 19




