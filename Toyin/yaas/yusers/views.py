from rest_framework import viewsets, views, status
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from yusers.models import *
from yusers.serializers import *

# class ActorsViewSet(viewsets.ModelViewSet):
#     queryset = Actors.objects.all()
#     serializer_class = ActorsSerializer

# def debby(request):
#     info = Actors.objects.all()
#     return HttpResponse(info)



# class ActorsView(ListAPIView):
#     serializer_class = ActorsSerializer
#     queryset = Actors.objects.all()


class ActorCreateAPIView(CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class ActorGetAPIView(RetrieveAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
    lookup_field = 'actor_id'

class ActorUpdateAPIView(UpdateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
    lookup_field = 'actor_id'

class ActorDeleteAPIView(DestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
    lookup_field = 'actor_id'



# class ActorViewAll(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actors.objects.all()
#     lookup_field = 'id'
#     serializer_class = ActorsSerializer

#     def delete(self, request, *args, **kwargs):
#         try:
#             id = request.data.get("")
#             passexcept Exception as e:
#             pass       

# class PostDetailAPIView(RetrieveAPIView):
#     queryset = post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"

#     def delete(self, request, id):
#         queryset = get.object_or_404(post, id=id)
#         queryset.delete()

# class PostUpdateAPIView(RetreiveUpdateAPIView):
#     queryset = post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"



class ActorsView(APIView):

    def get(self, request):
        serializer_class = ActorsSerializer
        allactors = Actors.objects.all().values()
        return Response({"detail":"Actor's Profile", "results":allactors})  

    def post(self, request):
        serializer_obj = ActorsSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Actors.objects.create(actor_id = serializer_obj.data.get("actor_id"),
            name = serializer_obj.data.get("name"),
            email = serializer_obj.data.get("email"),
            password = serializer_obj.data.get("password")
            )
        actor=Actors.objects.all().filter(actor_id = request.data["actor_id"]).values()
        return Response({"Message":"New Actor Added", "Actor":actor}) 


class ActorsDetail(APIView):

    def get_user(self, actor_id):
        try:
            actor = Actors.objects.get(actor_id= actor_id)
            return actor
        except Actors.DoesNotExist:
            return


    def get(self, request, actor_id):
        if not self.get_user(actor_id):
            Response(f'Actor with {actor_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = ActorsSerializer(self.get_user(actor_id))
        return Response(serializer.data)  


    def put(self, request, actor_id):
        
        serializer= ActorsSerializer(self.get_user(actor_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, actor_id):
        actor = self.get_user(actor_id)
        actor.delete()
        return Response(f"Actor's details deleted", status=status.HTTP_204_NO_CONTENT)

        #     Actors.objects.create(actor_id = serializer_obj.data.get("actor_id"),
        #     name = serializer_obj.data.get("name"),
        #     email = serializer_obj.data.get("email"),
        #     password = serializer_obj.data.get("password")
        #     )
        # actor=Actors.objects.all().filter(actor_id = request.data["actor_id"]).values()
        # return Response({"Message":"New Actor Added", "Actor":actor}) 







    # def put(self, request, pk):
    #     saved_actor = get_object_or_404(Actors.objects.all(), pk=pk)
    #     data = request.data.get('actors')
    #     serializer = ActorsSerializer(instance=saved_article, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         actor_saved = serializer.save()
    #     return Response({"success": "Actors '{}' updated successfully".format(actor_saved.title)})


# class DancingView(APIView):

#     def get(self, request):
#         dancing = Dancing.objects.first()
#         return Response({"dancing":DancingSerializer(dancing).data})  

#     def post(self, request, format=None):
#         serializer = DancingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DancingCreateView(views.APIView):

#     serializer_class = DancingSerializer

#     def post(self, request):
#         name = request.data["name"]
#         email = request.data["email"]
#         password = request.data["password"]
#         user = Dancing.objects.create(name=name, email=email, password=password)

#         return HttpResponse(user) 
        

    # """ this does the same as above
    # def get(self, request):
    #     dancing = Dancing.objects.all()
    #     serializer = DancingSerializer(dancing, many=True)
    #     return Response({"dancing": serializer.data}) 
    # """

    # def post(self, request):
    #     user = Dancing.objects.create(
    #             name=request.data.get('name'),
    #             email=request.data.get('email'),
    #             password=request.data.get('password'),
    #         )
    #     user.set_password(str(request.data.get('password')))
    #     user.save()
    #     return Response({"status":"success","response":"Successfully Created"})


    
    # def post(self, request):
    #     serializer = DancingSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     dancing = request.data.get('dancing')

    #     # Create an article from the above data
    #     serializer = DancingSerializer(data=dancing)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "user '{}' created successfully".format(article_saved.name)})


    # def put(self, request, pk):
    #     saved_article = get_object_or_404(Dancing.objects.all(), pk=pk)
    #     data = request.data.get('user')
    #     serializer = DancingSerializer(instance=saved_article, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Dancing '{}' updated successfully".format(article_saved.name)})


    # def delete(self, request, pk):
    # # Get object with this pk
    #     article = get_object_or_404(Dancing.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({"message": "Dancing with id `{}` has been deleted.".format(pk)},status=204)





# class DancingNew(APIView):
#     serializer_class = DancingSerializer
    
    # def get_object(self, pk):
    #     try:
    #         return Dancing.objects.get(pk=pk)
    #     except Dancing.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     dancing = self.get_object(pk)
    #     serializer = DancingSerializer(dancing)
    #     return Response(serializer.data)

    # def patch(self, request, pk, format=None):
    #     dancing = Dancing.objects.get(id=pk)
    #     serializer = DancingSerializer(dancing, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     dancing = self.get_object(pk)
    #     dancing.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



#### Going forward
 #1. Create a new django project called 'yaas'
 #2. Add a new app for users called yusers.
 #3. Add an endpoint to create a user
 #4. Add an endpoint to get a user
 #4. Add an endpoint to update a user
 #5. Add an endpoint to delete a user

 #Note: All endpoints must be individual CRUD using API view. Responses must be properly serialized / JSON.
          