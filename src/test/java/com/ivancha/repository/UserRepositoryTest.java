package com.ivancha.repository;

import com.ivancha.entity.User;
import com.ivancha.repository.UserRepository;
import com.ivancha.util.HibernateTestUtil;
import com.ivancha.util.TestDataImporter;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.junit.jupiter.api.*;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
// Методы, наследуемые от RepositoryBase тестировать не требуется. Они тестируются уже в классе PasswordRepositoryTest
public class UserRepositoryTest {

    private final SessionFactory sessionFactory = HibernateTestUtil.buildSessionFactory();
    private final Session userRepositorySession = sessionFactory.openSession();
    private final UserRepository userRepository = new UserRepository(userRepositorySession);

    @BeforeAll
    public void initDb() {
        TestDataImporter.importData(sessionFactory.getCurrentSession());
    }

    @AfterAll
    public void closeDb() {
        userRepositorySession.close();
        sessionFactory.close();
    }

    @BeforeEach
    public void openTransaction() {
        userRepositorySession.beginTransaction();
    }

    @AfterEach // так по мимо того, что не нужно будет работать с транзакциями в каждом методе,
    // транзакция будет откатываться в любом случае, даже если тест не прошёл (вроде).
    public void closeTransaction() {
        userRepositorySession.getTransaction().rollback();
    }


    @Test
    public void shouldFindByNickname() {
        var mayBeDima = userRepository.findByNickname("Dima");

        assertThat(mayBeDima).isNotEmpty();
        assertThat(mayBeDima.get().getNickname()).isEqualTo("Dima");
    }


    @Test
    public void bdShouldSetId() {
        var testUser = User.builder()
                .nickname("TestUser")
                .build();

        userRepository.save(testUser);

        assertThat(testUser.getId()).isNotNull();
    }


    @Test
    public void shouldDeleteUser() {
        var iliya = userRepository.findByNickname("Iliya");

        assertThat(iliya).isNotEmpty();
        userRepository.delete(iliya.get());

        var emptyIliya = userRepository.findByNickname("Iliya");
        assertThat(emptyIliya).isEmpty();
    }


    @Test
    public void shouldUpdateUser() {
        var petyaOptional = userRepository.findByNickname("Petya");
        assertThat(petyaOptional).isNotEmpty();

        var petya = petyaOptional.get();
        petya.setNickname("Roma");

        userRepository.update(petya);

        var updatedPetya = userRepository.findByNickname("Roma");
        assertThat(updatedPetya).isNotEmpty();
        assertThat(updatedPetya.get().getNickname()).isEqualTo("Roma");
    }

    @Test
    public void shouldFindAll() {
        List<User> allUsers = userRepository.findAll();
        assertThat(allUsers.stream()
                .map(User::getNickname)).containsExactlyInAnyOrderElementsOf(List.of("Dima", "Vova", "Andrey", "Petya", "Iliya"));
    }


    @Test
    public void shouldFindById() {
        var mayBeVova = userRepository.findById(2);

        assertThat(mayBeVova).isNotEmpty();
        assertThat(mayBeVova.get().getNickname()).isEqualTo("Vova");
    }

}
