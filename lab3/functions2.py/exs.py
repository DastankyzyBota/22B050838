#task1
def check_IMDB(a):
    if(a['imdb']>5.5):
        return True 
    else:
        return False
        print('Check if Detective is greater than 5.5') 
        is_g = check_IMDB(movies[12])
        if(is_g):
            print('True')
        else:
            print('False')

#task2
    list = []
    for i in range(0,len(a)):
        movie = a[i]
        if movie['imdb']>5.5:
            list.append(movie)
            return list
            print ('List of movies with an IMDB score > 5.5: ')
            list = sublist_IMDB(a)
            print(list)

#task3
def movies_category(movies, categories):
    list = []
    for i in movies:
        curr = i['cat']
        if categories.lowwer() == curr.lower():
            list.append(i)
            return list
            print('Movies in Romance are: ')
            list = movies_category(movies, 'Romance')
            print(list)

#task 4
def average_of_IMDB(movies):
    a=0
    mov = len(movies)
    for i in movies:
        a= a+ i['imdb']
        a= a/mov
        return a
        print('Average imdb is: ')
        b = average_of_IMDB(movies)
        print(b)

#task 5
def avg_imdb_acc_to_cat(movies,cat_name): 
    cat_movies=return_movie_category(movies,cat_name)
    avg_score=avg_imdb_score(cat_movies)
    return avg_score
    print('Average of Romance is: ')
    a=avg_imdb_acc_to_cat(movies,'Romance')
print(a)