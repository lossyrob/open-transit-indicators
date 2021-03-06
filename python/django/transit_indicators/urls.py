from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from datasources import views as datasourcesviews
from userdata import views as userviews
import views as indicatorviews

router = DefaultRouter()
router.register(r'gtfs-feeds', datasourcesviews.GTFSFeedViewSet)
router.register(r'gtfs-feed-problems', datasourcesviews.GTFSFeedProblemViewSet)
router.register(r'boundaries', datasourcesviews.BoundaryViewSet)
router.register(r'boundary-problems', datasourcesviews.BoundaryProblemViewSet)
router.register(r'demographics', datasourcesviews.DemographicDataSourceViewSet)
router.register(r'demographics-features', datasourcesviews.DemographicDataFeatureViewSet)
router.register(r'demographics-problems', datasourcesviews.DemographicDataSourceProblemViewSet)
router.register(r'osm-data', datasourcesviews.OSMDataViewSet, base_name='osm-data')
router.register(r'osm-data-problems', datasourcesviews.OSMDataProblemsViewSet, base_name='osm-data-problems')
router.register(r'users', userviews.OTIUserViewSet, base_name='users')
router.register(r'config', indicatorviews.OTIIndicatorsConfigViewSet, base_name='config')
router.register(r'config-demographic', indicatorviews.OTIDemographicConfigViewSet)
router.register(r'sample-periods', indicatorviews.SamplePeriodViewSet, base_name='sample-periods')
router.register(r'indicators', indicatorviews.IndicatorViewSet)

urlpatterns = patterns('',  # NOQA
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'userdata.views.obtain_auth_token'),
    url(r'^api/indicators_version/', 'transit_indicators.views.indicators_version')
)
