from django.shortcuts import render,redirect
from .models import todomodel
from .forms import todoform

def todoview(request):

	form = todoform()


	if request.method == 'POST':
		form=todoform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	

	todo=todomodel.objects.all()
	context={'todo':todo,'forms':form}
	return render(request,'todo/did.html',context)





def updatetodoview(request,pk):
	task = todomodel.objects.get(id=pk)
	form = todoform(instance=task)

	if request.method == 'POST':
		form = todoform(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'task':task,'form':form}
	return render(request,'todo/update.html',context)

def deletetodoview(request,pk):
	item = todomodel.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('home')
	context={'item':item}
	return render(request,'todo/delete.html',context)



