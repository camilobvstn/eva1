from django.shortcuts import render

# Create your views here.

def main(request):
    return render (request,'myapp/index.html')

def manzana(request):
    data={"nombre":"Tarta de Manzana", "desc":"Una deliciosa tarta de manzana","img_1":"mazana.jpeg"}
    return render(request,'myapp/recetas.html',data)

def paella(request):
    data={"nombre":"Paella", "desc":"Un delicioso plato tipico español","img_1":"paella.jpeg"}
    return render(request,'myapp/recetas.html',data)

def pizza(request):
    data={"nombre":"Pizza", "desc":"Un delicioso plato tipico italiano","img_1":"pizza.jpeg"}
    return render(request,'myapp/recetas.html',data)