from facegram.posts.tests.factories import PostFactory


class PostFactoryWorker:
    @staticmethod
    def create_test_post():
        return PostFactory()
    
    @staticmethod
    def create_test_posts(number_of_posts: int = 3):
        return PostFactory.create_batch(number_of_posts)