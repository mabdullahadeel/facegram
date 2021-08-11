import { Flex, Heading, Button, useColorMode, useColorModeValue } from '@chakra-ui/react';
import { AiOutlineGithub } from 'react-icons/ai';

function Login() {
    const { toggleColorMode } =  useColorMode();
    const formBackground = useColorModeValue("gray.100", "gray.700");
    return (
        <Flex
            height="100vh"
            alignItems="center"
            justifyContent="center"
        >
            <Flex
                direction="column"
                alignItems="center"
                background={formBackground}
                p={12}
                rounded={6}
            >
                <Heading
                    mb={6}
                >
                    Log in
                </Heading>
                <Button 
                    colorScheme={useColorModeValue("blackAlpha", "whiteAlpha")}
                    leftIcon={<AiOutlineGithub />}
                    color="white"
                    mb={6}
                >
                    Log in with GitHub
                </Button>
                <Button
                    width="100%"
                    colorScheme="teal"
                    onClick={toggleColorMode}
                    variant="outline"
                >
                    Toggle Theme
                </Button>
            </Flex>
        </Flex>
    )
}

export default Login;
