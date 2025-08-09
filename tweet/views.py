from django.shortcuts import redirect, render

import tweet
from tweet.forms import TweetForm


def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            # tweet = form.cleaned_data['tweet']
            tweet.save()
            return redirect()

    else:
        form = TweetForm()

    return render(request, 'tweet.html', {'form': form})

# def tweets(request):
#     create_tweet = TweetForm(request.POST or None)
#     if create_tweet.is_valid():
#     tweet = form.cleaned_data['tweet']
#             tweet.save()
#             return redirect()
#
#     else:
#         form = TweetForm()
#
#     return render(request, 'tweet.html', {'form': form})