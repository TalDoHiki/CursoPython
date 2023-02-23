wg = float(input('Type your weight: '))
hg = float(input('Type your height: '))
st = str
imc = wg / (hg**2)

if imc < 18.5:
    st = 'lower than average'
elif imc >= 18.5 and imc <= 25:
    st = 'ideal'
elif imc > 25 and imc <= 30:
    st = 'overweight'
elif imc > 30 and imc <= 40:
    st = 'obesity'
elif imc > 40:
    st = 'morbid obesity'

print('''
IMC Status: {}
IMC Index: {:.1f}'''.format(st,imc))