from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Business, Neighborhood, Meeting

# Create your tests here.
class AppTestClass(TestCase):

    def setUp(self):
        self.new_user = User(id = 1, first_name = 'James', last_name = 'Bond', username = 'jamie', email = 'jamesbond@gmail.com')
        # self.new_user.save()

        self.new_hood = Neighborhood(id = 1, neighborhood_name = 'TestArea',image = 'neighbor.jpg', location = 'Location', occupants = 20)
        # self.new_hood.save()

        self.new_business = Business(id = 1, name = 'Test', image = 'photo.jpg',description= 'Test project', user = self.new_user, neighbor = self.new_hood, business_email = 'bizz@gmail.com')
        # self.new_business.save()

        self.new_profile = Profile(id = 1, user = self.new_user, family_name = 'Test Name', family_members = 5, family_email = 'family@gmail.com', profile_photo = 'save.jpg',hood = self.new_hood)
        # self.new_profile.save()

        self.new_post = Meeting(id = 1, title = 'Title', content = 'Bang Bang', user = self.new_user, hood = self.new_hood)
        # self.new_review.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Meeting.objects.all().delete()
        Business.objects.all().delete()
        Neighborhood.objects.all().delete()

    def test_instance_user(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_instance_meeting(self):
        self.assertTrue(isinstance(self.new_post, Meeting))

    def test_instance_business(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_instance_hood(self):
        self.assertTrue(isinstance(self.new_hood, Neighborhood))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    
    def test_save_business(self):
        self.new_business.save_business()
        bizz = Business.objects.all()
        self.assertTrue(len(bizz) > 0)

    def test_save_hood(self):
        self.new_hood.save_neighborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_save_post(self):
        self.new_post.save_meeting()
        post = Meeting.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_profile(self):
        profile = self.new_profile
        profile.save_profile()
        profile.delete_profile()        
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_delete_hood(self):
        hood = self.new_hood
        hood.save()
        hood.delete_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) == 0)

    def test_delete_business(self):
        bizz = self.new_business
        bizz.save_business()
        bizz.delete_business()        
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_delete_meeting(self):
        post = self.new_post
        post.save_meeting()
        post.delete_meeting()        
        self.assertTrue(len(Meeting.objects.all()) == 0)

    def test_update_profile_photo(self):
        self.new_profile.save()
        profile = Profile.objects.last().id
        Profile.update_profile_photo(profile, 'jpg@gmail.com')
        new = Profile.objects.get(id = profile)
        self.assertEqual(new.family_email, 'jpg@gmail.com')

    def test_update_neighborhood(self):
        self.new_hood.save()
        hood_id = Neighborhood.objects.last().id
        Neighborhood.update_neighborhood_name(hood_id, 'Testing2')
        new = Neighborhood.objects.get(id = hood_id)
        self.assertEqual(new.neighborhood_name, 'Testing2')

    def test_update_occupants(self):
        self.new_hood.save()
        hood_id = Neighborhood.objects.last().id
        Neighborhood.update_neighborhood_occupants(hood_id, 10)
        new = Neighborhood.objects.get(id = hood_id)
        self.assertEqual(new.occupants, 10)
    
    def test_update_business(self):
        self.new_business.save()
        bizz_id = Business.objects.last().id
        Business.update_business_name(bizz_id, 'cloud9')
        new = Business.objects.get(id = bizz_id)
        self.assertEqual(new.name, 'cloud9')

    def test_hood_search_by_name(self):
        self.new_hood.save()
        hood = Neighborhood.search_neighborhood('TestArea')
        self.assertTrue(len(hood)== 1)

    def test_profile_search_by_username(self):
        self.new_user.save()
        profile = Profile.search_username('jamie')
        self.assertTrue(len(profile)== 1)

    def test_business_search_by_name(self):
        self.new_business.save()
        bizz = Business.search_business('Test')
        self.assertTrue(len(bizz)== 1)