#Anyla Reeves
#3/12/25
#Period:5

#init
#function
#main
import random
Track_name = ["tv off (feat. lefty gunplay)", "reincarnated", "WILDFLOWER", "Timeless (with Playboi Carti)", "That's What I Like", "heart pt. 6","Sticky (feat. GloRilla, Sexyy Red & Lil Wayne)","BIRDS OF A FEATHER", "Ma Meilleure Ennemie (from the series Arcane League of Legends)","Who"]
Songs_Artist = ["Kendrick Lamar", "Kendrick Lamar", "Billie Eilish", "The Weeknd", "Bruno Mars", "Kendrick Lamar", "Tyler, The Creator","Billie Eilish","Stromae", "Jimin"]
filtered_list =[]

#Ask user what type of genre they are look for
#Hip-Hop/Rap
#R&B/Soul
#Pop Electropop
#Jazz Rap/Horrorcore
#K-Pop

#Loop through the Songs Artist finding their genre
#for i in range(len(Song_Artist)): #This is great because we want the artist of the genre
#if song_Artist[1]<=Kendrick Lamar: #Hip-Hop/Rap
#filtered_list.append(Track_name[1])
#append track name to the same index to the filtered list
#print(filtered_list)
#for artist for songs_artist: this won't be a good thing to code because its not sure of what it really is asking
#When you find a song, add what track name to the filtered list

def music_genre(genre):
    #x = input("what type of music genre are you looking for(Hip-Hop/Rap, R&B/Soul, Pop Electropop, Jazz Rap/Horrorcore, K-Pop):")
    if genre == "Hip-Hop/Rap":
        for i in range (len(Songs_Artist)):
            if Songs_Artist[i]=="Kendrick Lamar":
                filtered_list.append(Track_name[i])
        print(random.choice(filtered_list) + " by Kendrick Lamar ")

    if genre == "R&B/Soul":
        for i in range(len(Songs_Artist)):
            if Songs_Artist[i]=="The Weeknd":
                filtered_list.append(Track_name[i])
        print(random.choice(filtered_list) + " by The Weekend ")

    if genre == "Pop Electropop":
        for i in range(len(Songs_Artist)):
            if Songs_Artist[i]=="Billie Eilish":
                filtered_list.append(Track_name[i])
        print(random.choice(filtered_list) + " by Billie Ellish ")

    if genre == "Jazz Rap/Horrorcore":
        for i in range(len(Songs_Artist)):
            if Songs_Artist[i]=="Tyler, The Creator":
                filtered_list.append(Track_name[i])
        print(random.choice(filtered_list) + " by Tyler, The Creator ")

    if genre == "K-Pop":
        for i in range (len(Songs_Artist)):
            if Songs_Artist[i]=="Jimin":
                filtered_list.append(Track_name[i])
        print(random.choice(filtered_list) + " by Jimin ")

#Main
music_genre(input("what type of music genre do you want to listen to: Hip-Hop/Rap, R&B/Soul, Pop Electropop, Jazz Rap/Horrorcore, K-Pop" ))

