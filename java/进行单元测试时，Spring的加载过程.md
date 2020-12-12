进行单元测试时，Spring的加载过程。
```
public class TestUserDao extends TestBaseDao {
	@Autowired
	private User2Dao userDao;

	@Test
	public void testGetUsers() {
		List<Map<String, Object>> l = userDao.getUsers();
		int cnt = l.size();
		assertTrue(cnt > 0);
	}

	@Test
	public void testGetUsersDomain() {
		List<UserDomain> users = userDao.getUsersDomain();
		for (UserDomain user : users) {
			System.out.println(String.format("user:%s	%s	%s", user.getId(),
					user.getName(), user.getAge()));
		}
		int cnt = users.size();
		assertTrue(cnt > 0);
	}

	@Test
	public void testGetUserById() {
		Map<String, Object> params = new HashMap<String, Object>();
		params.put("id", "1");
		Map<String, Object> l = userDao.getUserById(params);
		String name = (String) l.get("name");
		assertTrue(!name.isEmpty());
	}

	@Test
	public void testGetUserById2() {
		UserDomain u = new UserDomain();
		u.setId(1);
		UserDomain ru = userDao.getUserById2(u);
		String name = ru.getName();
		assertTrue(!name.isEmpty());
	}

	@Test
	public void testAddBatch() {
		List<UserDomain> users = new ArrayList<UserDomain>();
		users.add(new UserDomain("1", 1));
		users.add(new UserDomain("2", 2));
		users.add(new UserDomain("3", 3));
		users.add(new UserDomain("4", 4));
		users.add(new UserDomain("5", 5));
		userDao.addBatch(users);

		int cnt = users.size();
		cnt = 1;
		assertTrue(true);
	}

	/**
	 * 所有测试开始之前运行
	 * 
	 * 必须为静态方法
	 */
	@BeforeClass
	public static void setUpBeforeClass() {
		System.out.println("访问test2数据库...");
	}

	/**
	 * 每一个测试方法之前运行
	 * 
	 * @throws Exception
	 */
	@Before
	public void setUp() throws Exception {
		System.out.println("测试中...");
	}

	/**
	 * 每一个测试方法之后运行
	 */
	@After
	public void tearDown() {
		System.out.println("...");
	}

	/**
	 * 所有测试结束之后运行
	 * 
	 * 必须为静态方法
	 */
	@AfterClass
	public static void tearDownAfterClass() {
		System.out.println("访问test2数据库...END");
	}
}

```
```
[ INFO] [2017-05-19 11:54:28 292] [main] (TestContextManager.java:185) @TestExecutionListeners is not present for class [class com.baobaotao.web.dao.test2.TestUserDao]: using defaults.
访问test2数据库...
[ INFO] [2017-05-19 11:54:28 456] [main] (XmlBeanDefinitionReader.java:315) Loading XML bean definitions from class path resource [spring-config.xml]
[ INFO] [2017-05-19 11:54:28 710] [main] (XmlBeanDefinitionReader.java:315) Loading XML bean definitions from class path resource [spring-config-servlet.xml]
[ INFO] [2017-05-19 11:54:28 738] [main] (XmlBeanDefinitionReader.java:315) Loading XML bean definitions from class path resource [spring-config-dao.xml]
[ INFO] [2017-05-19 11:54:28 766] [main] (AbstractApplicationContext.java:503) Refreshing org.springframework.context.support.GenericApplicationContext@97e121c: startup date [Fri May 19 11:54:28 CST 2017]; root of context hierarchy
[ INFO] [2017-05-19 11:54:28 912] [main] (PropertiesLoaderSupport.java:177) Loading properties file from class path resource [conf/jdbc.properties]
[ INFO] [2017-05-19 11:54:28 913] [main] (PropertiesLoaderSupport.java:177) Loading properties file from class path resource [conf/app.properties]
[ INFO] [2017-05-19 11:54:28 990] [main] (DefaultListableBeanFactory.java:577) Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@663b1f38: defining beans [appConfig,jsonUtil,userService,org.springframework.context.annotation.internalConfigurationAnnotationProcessor,org.springframework.context.annotation.internalAutowiredAnnotationProcessor,org.springframework.context.annotation.internalRequiredAnnotationProcessor,org.springframework.context.annotation.internalCommonAnnotationProcessor,org.springframework.aop.config.internalAutoProxyCreator,propertyConfigurer,abstractDataSource,testDataSource,test2DataSource,transactionManager,transactionManager2,testSessionFactory,test2SessionFactory,org.mybatis.spring.mapper.MapperScannerConfigurer#0,org.mybatis.spring.mapper.MapperScannerConfigurer#1,org.springframework.context.annotation.ConfigurationClassPostProcessor.importAwareProcessor,authDao,userDao,user2Dao]; root of factory hierarchy
测试中...
...
测试中...
...
测试中...
...
测试中...
...
测试中...
...
访问test2数据库...END
[ INFO] [2017-05-19 11:54:29 977] [Thread-3] (AbstractApplicationContext.java:1032) Closing org.springframework.context.support.GenericApplicationContext@97e121c: startup date [Fri May 19 11:54:28 CST 2017]; root of context hierarchy
[ INFO] [2017-05-19 11:54:29 978] [Thread-3] (DefaultSingletonBeanRegistry.java:434) Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@663b1f38: defining beans [appConfig,jsonUtil,userService,org.springframework.context.annotation.internalConfigurationAnnotationProcessor,org.springframework.context.annotation.internalAutowiredAnnotationProcessor,org.springframework.context.annotation.internalRequiredAnnotationProcessor,org.springframework.context.annotation.internalCommonAnnotationProcessor,org.springframework.aop.config.internalAutoProxyCreator,propertyConfigurer,abstractDataSource,testDataSource,test2DataSource,transactionManager,transactionManager2,testSessionFactory,test2SessionFactory,org.mybatis.spring.mapper.MapperScannerConfigurer#0,org.mybatis.spring.mapper.MapperScannerConfigurer#1,org.springframework.context.annotation.ConfigurationClassPostProcessor.importAwareProcessor,authDao,userDao,user2Dao]; root of factory hierarchy
[ INFO] [2017-05-19 11:54:29 980] [Thread-3] (BoneCP.java:156) Shutting down connection pool...
[ INFO] [2017-05-19 11:54:29 982] [Thread-3] (BoneCP.java:177) Connection pool has been shutdown.
[ INFO] [2017-05-19 11:54:29 983] [Thread-3] (BoneCP.java:156) Shutting down connection pool...
[ INFO] [2017-05-19 11:54:29 984] [Thread-3] (BoneCP.java:177) Connection pool has been shutdown.

```